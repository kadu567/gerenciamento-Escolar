from flask import Flask
from models import db, Usuario
from sqlalchemy.exc import SQLAlchemyError
import time
import os  # Adicione esta linha

def create_app():
    app = Flask(__name__)

    # Adicione estas linhas para configurar a chave secreta
    app.secret_key = os.environ.get('SECRET_KEY') or 'uma_chave_secreta_muito_secreta'

    # Configuração do banco de dados
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://app_user:QWxVbk9zVERz@alunostds.dev.br:3308/app_user'
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
        'pool_recycle': 280,
        'pool_timeout': 20,
        'pool_pre_ping': True
    }
    
    # Inicializar a instância do banco de dados
    db.init_app(app)

    # Função para testar a conexão
    def test_db_connection():
        max_retries = 3
        retry_delay = 2

        for attempt in range(max_retries):
            try:
                with app.app_context():
                    db.engine.connect()
                print("Conexão com o banco de dados estabelecida com sucesso!")
                return True
            except SQLAlchemyError as e:
                if attempt < max_retries - 1:
                    print(f"Erro de conexão: {e}. Tentando novamente em {retry_delay} segundos...")
                    time.sleep(retry_delay)
                else:
                    print(f"Falha ao conectar ao banco de dados após {max_retries} tentativas: {e}")
                    return False

    # Testar a conexão antes de registrar as rotas
    if test_db_connection():
        # Importar e registrar os Blueprints
        from routes import main_routes, auth_routes
        app.register_blueprint(main_routes)
        app.register_blueprint(auth_routes)
    else:
        @app.route('/')
        def db_error():
            return "Erro de conexão com o banco de dados. Por favor, verifique as configurações e tente novamente."

    with app.app_context():
        # novo_usuario = Usuario.criar_usuario(nome='Kelvin', cargo='cantor de boyband', email='kelvin@gmail.com', senha='senha1')
        # db.session.add(novo_usuario)
        # db.session.commit()  # Não esqueça de confirmar a sessão
        pass

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
    
