"""Generated from Smithy shape ``com.amazonaws.appflow#BasicAuthCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.password
    import capo_appflow.types.username


class BasicAuthCredentials(TypedDict, closed=True):
    username: "capo_appflow.types.username.Username"
    """<p> The username to use to connect to a resource. </p>"""
    password: "capo_appflow.types.password.Password"
    """<p> The password to use to connect to a resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BasicAuthCredentials) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> BasicAuthCredentials:
    out: BasicAuthCredentials = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError("BasicAuthCredentials.username required")
    if "password" in data:
        out["password"] = data["password"]
    else:
        raise DeserializationError("BasicAuthCredentials.password required")
    return out
