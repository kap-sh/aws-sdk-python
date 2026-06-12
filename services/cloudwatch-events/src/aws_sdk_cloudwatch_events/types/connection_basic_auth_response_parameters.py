"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionBasicAuthResponseParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cloudwatch_events.types.auth_header_parameters


class ConnectionBasicAuthResponseParameters(TypedDict):
    username: NotRequired[
        "aws_sdk_cloudwatch_events.types.auth_header_parameters.AuthHeaderParameters"
    ]
    """<p>The user name to use for Basic authorization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionBasicAuthResponseParameters) -> dict:
    out: dict = {}
    if "username" in value:
        out["Username"] = value["username"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionBasicAuthResponseParameters:
    out: ConnectionBasicAuthResponseParameters = {}  # type: ignore[typeddict-item]
    if "Username" in data:
        out["username"] = data["Username"]
    return out
