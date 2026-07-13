from forgetree import generate

tree = """
backend/
    app/
    main.py
"""

generate(tree, "project")