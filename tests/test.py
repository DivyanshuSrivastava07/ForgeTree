from forgetree.parser import Parser
# from scaffold.tree_printer import TreePrinter
from forgetree.builder import Builder
from forgetree.writer import FileSystemWriter

text = """
backend/

    app/
        main.py

        
        
        api/
            auth.py
            users.py
            predict.py

        models/
            user.py
            prediction.py

        schemas/

        services/
            auth.py
            ai.py
            image.py

        database/
            db.py

        middleware/

        utils/

    uploads/

    model/

requirements.txt
"""
nodes = Parser().parse(text)
roots = Builder().build(nodes)

FileSystemWriter().write(roots,"python")
