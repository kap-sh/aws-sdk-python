"""Generated from Smithy shape ``com.amazonaws.appflow#VeevaConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.password
    import capo_appflow.types.username


class VeevaConnectorProfileCredentials(TypedDict, closed=True):
    username: "capo_appflow.types.username.Username"
    """<p> The name of the user. </p>"""
    password: "capo_appflow.types.password.Password"
    """<p> The password that corresponds to the user name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VeevaConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> VeevaConnectorProfileCredentials:
    out: VeevaConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError("VeevaConnectorProfileCredentials.username required")
    if "password" in data:
        out["password"] = data["password"]
    else:
        raise DeserializationError("VeevaConnectorProfileCredentials.password required")
    return out
