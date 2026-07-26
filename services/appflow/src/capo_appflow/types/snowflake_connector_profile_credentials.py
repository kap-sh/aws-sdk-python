"""Generated from Smithy shape ``com.amazonaws.appflow#SnowflakeConnectorProfileCredentials``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_appflow.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appflow.types.password
    import capo_appflow.types.username


class SnowflakeConnectorProfileCredentials(TypedDict, closed=True):
    username: "capo_appflow.types.username.Username"
    """<p> The name of the user. </p>"""
    password: "capo_appflow.types.password.Password"
    """<p> The password that corresponds to the user name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnowflakeConnectorProfileCredentials) -> dict:
    out: dict = {}
    out["username"] = value["username"]
    out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> SnowflakeConnectorProfileCredentials:
    out: SnowflakeConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    else:
        raise DeserializationError(
            "SnowflakeConnectorProfileCredentials.username required"
        )
    if "password" in data:
        out["password"] = data["password"]
    else:
        raise DeserializationError(
            "SnowflakeConnectorProfileCredentials.password required"
        )
    return out
