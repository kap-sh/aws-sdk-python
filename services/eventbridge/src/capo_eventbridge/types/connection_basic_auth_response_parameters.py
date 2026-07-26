"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionBasicAuthResponseParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eventbridge.types.auth_header_parameters


class ConnectionBasicAuthResponseParameters(TypedDict, closed=True):
    username: NotRequired[
        "capo_eventbridge.types.auth_header_parameters.AuthHeaderParameters"
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
