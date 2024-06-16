import sqlite3
from database.conexao import Conexao


class SalaDeAulaModel:
    def __init__(self):
        self.db = Conexao()

    def consultar_por_id_salas(self, id_sala):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT ga.id, p.nome AS professor, d.nome AS disciplina, ga.horario, d.id
                FROM grade_aulas ga
                JOIN professor p ON ga.id_professor = p.id
                JOIN disciplina d ON ga.id_disciplina = d.id
                WHERE ga.id = ?
            '''
            self.db.executar_sql(query, (id_sala,))
            salas_do_aluno = self.db.fetchall()
            return salas_do_aluno
        except sqlite3.Error as e:
            print(f"Erro ao consultar salas de aula por aluno: {e}")
        finally:
            self.db.fechar_conn()
     
    def consultar_salas_aulas(self):
        try: 
            self.db.iniciar_conn()
           
            query = '''
            SELECT ga.id, p.nome AS professor,d.nome AS disciplina, ga.horario, d.id
            FROM grade_aulas ga
            JOIN professor p ON ga.id_professor = p.id
            JOIN disciplina d ON ga.id_disciplina = d.id
            '''
            self.db.executar_sql(query)

            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e.args[0]}")
        finally:
            self.db.fechar_conn()

    def consultar_alunos_aula(self, id_aula):
        try:
            self.db.iniciar_conn()
            query = '''
            SELECT a.id, a.nome, a.endereco
            FROM salas_aulas sa
            JOIN aluno a ON sa.id_aluno = a.id
            WHERE sa.id_aula = ?
            '''
            self.db.executar_sql(query, (id_aula,))
            return self.db.fetchall()
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e}")
        finally:
            self.db.fechar_conn()

    def consultar_salas_por_aluno(self, aluno_id):
        try:
            self.db.iniciar_conn()
            query = """
                SELECT id_aula FROM salas_aulas WHERE id_aluno = ?
            """
            self.db.executar_sql(query, (aluno_id,))
            salas = self.db.fetchall()
            return [sala[0] for sala in salas]
        except sqlite3.Error as e:
            print(f"Ocorreu um erro durante a busca: {e}")
        finally:
            self.db.fechar_conn()
  
    def consultar_alunos_por_sala(self, id_sala):
        try:
            self.db.iniciar_conn()
            query = '''
                SELECT a.id, a.nome
                FROM aluno a
                JOIN salas_aulas sa ON a.id = sa.id_aluno
                WHERE sa.id = ?
            '''
            self.db.executar_sql(query, (id_sala,))
            alunos_da_sala = self.db.fetchall()
            return alunos_da_sala
        except sqlite3.Error as e:
            print(f"Erro ao consultar alunos por sala: {e}")
            return []
        finally:
            self.db.fechar_conn()   