from src.contas import Contas


class Test_Contas:

    def test_soma(self):
        result = Contas.soma(2, 3)
        assert result == 5
    def test_subtracao(self):
        result = Contas.subtracao(5, 3)
        assert result == 2
    def test_media(self):
        result = Contas.media(5, 3)
        assert result == 4