"""Generated from Smithy shape ``com.amazonaws.glue#BasicAuthenticationCredentials``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.password
    import aws_sdk_glue.types.username


class BasicAuthenticationCredentials(TypedDict):
    username: NotRequired["aws_sdk_glue.types.username.Username"]
    """<p>The username to connect to the data source.</p>"""
    password: NotRequired["aws_sdk_glue.types.password.Password"]
    """<p>The password to connect to the data source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BasicAuthenticationCredentials) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    if "password" in value:
        out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BasicAuthenticationCredentials:
    out: BasicAuthenticationCredentials = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    if "Password" in data:
        out["password"] = data["Password"]
    return out
