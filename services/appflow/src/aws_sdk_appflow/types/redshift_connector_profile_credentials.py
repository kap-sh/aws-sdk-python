"""Generated from Smithy shape ``com.amazonaws.appflow#RedshiftConnectorProfileCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appflow.types.password
    import aws_sdk_appflow.types.string


class RedshiftConnectorProfileCredentials(TypedDict):
    username: NotRequired["aws_sdk_appflow.types.string.String"]
    """<p> The name of the user. </p>"""
    password: NotRequired["aws_sdk_appflow.types.password.Password"]
    """<p> The password that corresponds to the user name. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedshiftConnectorProfileCredentials) -> dict:
    out: dict = {}
    if "username" in value:
        out["username"] = value["username"]
    if "password" in value:
        out["password"] = value["password"]
    return out


def deserialize_json(data: dict) -> RedshiftConnectorProfileCredentials:
    out: RedshiftConnectorProfileCredentials = {}  # type: ignore[typeddict-item]
    if "username" in data:
        out["username"] = data["username"]
    if "password" in data:
        out["password"] = data["password"]
    return out
