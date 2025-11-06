from src.main import main

def test_main_output():
    # On capture l'affichage
    import io, sys
    captured_output = io.StringIO()
    sys.stdout = captured_output
    main()
    sys.stdout = sys.__stdout__
    assert captured_output.getvalue().strip() == "Projet Python convert fonctionnel !"
