"""Generated from Smithy shape ``com.amazonaws.datazone#UsernamePassword``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datazone.types.password
    import capo_datazone.types.username


class UsernamePassword(TypedDict, closed=True):
    password: "capo_datazone.types.password.Password"
    """<p>The password of a connection.</p>"""
    username: "capo_datazone.types.username.Username"
    """<p>The username of a connection.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UsernamePassword) -> dict:
    out: dict = {}
    out["password"] = value["password"]
    out["username"] = value["username"]
    return out


def deserialize_json(data: dict) -> UsernamePassword:
    out: UsernamePassword = {}  # type: ignore[typeddict-item]
    if "password" in data:
        out["password"] = data["password"]
    else:
        raise DeserializationError("UsernamePassword.password required")
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError("UsernamePassword.username required")
    return out
