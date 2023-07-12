import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(1, 1)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("message", "wrong_key")

    assert encrypt_message("message", 10) == "egassem"

    assert encrypt_message("message", 3) == "sem_egas"
