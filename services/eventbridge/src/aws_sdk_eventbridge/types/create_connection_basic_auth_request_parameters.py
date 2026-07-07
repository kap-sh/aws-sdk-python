"""Generated from Smithy shape ``com.amazonaws.eventbridge#CreateConnectionBasicAuthRequestParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.auth_header_parameters
    import aws_sdk_eventbridge.types.auth_header_parameters_sensitive


class CreateConnectionBasicAuthRequestParameters(TypedDict, closed=True):
    username: "aws_sdk_eventbridge.types.auth_header_parameters.AuthHeaderParameters"
    """<p>The user name to use for Basic authorization.</p>"""
    password: "aws_sdk_eventbridge.types.auth_header_parameters_sensitive.AuthHeaderParametersSensitive"
    """<p>The password associated with the user name to use for Basic authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateConnectionBasicAuthRequestParameters) -> dict:
    out: dict = {}
    out["Username"] = value["username"]
    out["Password"] = value["password"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateConnectionBasicAuthRequestParameters:
    out: CreateConnectionBasicAuthRequestParameters = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    else:
        raise DeserializationError(
            "CreateConnectionBasicAuthRequestParameters.username required"
        )
    if "Password" in data:
        out["password"] = data["Password"]
    else:
        raise DeserializationError(
            "CreateConnectionBasicAuthRequestParameters.password required"
        )
    return out
