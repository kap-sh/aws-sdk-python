"""Generated from Smithy shape ``com.amazonaws.eventbridge#ConnectionOAuthClientResponseParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.auth_header_parameters


class ConnectionOAuthClientResponseParameters(TypedDict):
    client_id: NotRequired[
        "aws_sdk_eventbridge.types.auth_header_parameters.AuthHeaderParameters"
    ]
    """<p>The client ID associated with the response to the connection request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionOAuthClientResponseParameters) -> dict:
    out: dict = {}
    if "client_id" in value:
        out["ClientID"] = value["client_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionOAuthClientResponseParameters:
    out: ConnectionOAuthClientResponseParameters = {}  # type: ignore[typeddict-item]
    if "ClientID" in data:
        out["client_id"] = data["ClientID"]
    return out
