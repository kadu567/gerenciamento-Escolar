from flask import Blueprint, render_template, redirect, url_for, flash, session, request, send_from_directory
from models import *
from .auth import login_required

data_register = Blueprint('data_register', __name__)

@data_register.route('/data_register', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'POST':
        if 'cadastro_salas' in request.form:
            nome_sala = request.form['nomeSala']
            capacidade = request.form['capacidadeSala']
            tipo_sala = request.form['tipoSala']
            cor_sala = request.form['corSala']
            
            nova_sala = Sala(Nome=nome_sala, Capacidade=capacidade, Tipo=tipo_sala, Cor=cor_sala)
            db.session.add(nova_sala)
            db.session.commit()
            
            flash('Sala registrada com sucesso!', 'success')
        
        elif 'cadastro_turmas' in request.form:
            horario_inicio = request.form['horarioInicio']
            horario_fim = request.form['horarioFim']
            cor_turma = request.form['corTurma']
            
            nova_turma = Turma(HorarioInicio=horario_inicio, HorarioFim=horario_fim, Cor=cor_turma)
            db.session.add(nova_turma)
            db.session.commit()
            
            flash('Turma registrada com sucesso!', 'success')
        
        elif 'cadastro_predios' in request.form:
            nome_predio = request.form['nomePredio']
            andares = request.form['andaresPredio']
            cor_predio = request.form['corPredio']
            
            novo_predio = Predio(Nome=nome_predio, Andares=andares, Cor=cor_predio)
            db.session.add(novo_predio)
            db.session.commit()
            
            flash('Prédio registrado com sucesso!', 'success')
        
        elif 'cadastro_andares' in request.form:
            numero_andar = request.form['numeroAndar']
            predio_andar = request.form['predioAndar']
            cor_andar = request.form['corAndar']
            
            novo_andar = Andar(Numero=numero_andar, ID_predio=predio_andar, Cor=cor_andar)
            db.session.add(novo_andar)
            db.session.commit()
            
            flash('Andar registrado com sucesso!', 'success')
        
        return redirect(url_for('main.home'))
    
    return render_template('data_register.html')

@data_register.route('/register-professor', methods=['GET', 'POST'])
@login_required
def register_professor():
    if request.method == 'POST':
        nome_professor = request.form['nomeProfessor']
        area = request.form['areaProfessor']
        carga_horaria = request.form['cargaHoraria']
        tipo_contrato = request.form['tipoContrato']
        disponibilidade = request.form['disponibilidade']
        
        novo_professor = Professor(Nome=nome_professor, Area=area, CargaHoraria=carga_horaria, TipoContrato=tipo_contrato, Disponibilidade=disponibilidade)
        db.session.add(novo_professor)
        db.session.commit()
        
        flash('Professor registrado com sucesso!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('register_professor.html')

@data_register.route('/register-user', methods=['GET', 'POST'])
@login_required
def register_user():
    if request.method == 'POST':
        nome_usuario = request.form['nomeUsuario']
        cargo = request.form['cargoUsuario']
        email = request.form['emailUsuario']
        senha = request.form['senhaUsuario']
        
        novo_usuario = Usuario(Nome=nome_usuario, Cargo=cargo, Email=email, Senha=senha)
        db.session.add(novo_usuario)
        db.session.commit()
        
        flash('Usuário registrado com sucesso!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('register_user.html')

@data_register.route('/register-resource', methods=['GET', 'POST'])
@login_required
def register_resource():
    if request.method == 'POST':
        quantidade = request.form['quantidadeRecurso']
        identificacao = request.form['identificacaoRecurso']
        status = request.form['statusRecurso']
        
        novo_recurso = Recurso(Quantidade=quantidade, Identificacao=identificacao, Status=status)
        db.session.add(novo_recurso)
        db.session.commit()
        
        flash('Recurso registrado com sucesso!', 'success')
        return redirect(url_for('main.home'))
    
    return render_template('register_resource.html')
