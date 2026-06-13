"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadClientCredentialsGrantDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.client_id
    import aws_sdk_quicksight.types.endpoint


class ReadClientCredentialsGrantDetails(TypedDict):
    client_id: "aws_sdk_quicksight.types.client_id.ClientId"
    """<p>The client identifier for the OAuth2 client credentials grant flow.</p>"""
    token_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The authorization server endpoint used to obtain access tokens via the client credentials grant flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadClientCredentialsGrantDetails) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["TokenEndpoint"] = value["token_endpoint"]
    return out


def deserialize_json(data: dict) -> ReadClientCredentialsGrantDetails:
    out: ReadClientCredentialsGrantDetails = {}  # type: ignore[typeddict-item]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError(
            "ReadClientCredentialsGrantDetails.client_id required"
        )
    if "TokenEndpoint" in data:
        out["token_endpoint"] = data["TokenEndpoint"]
    else:
        raise DeserializationError(
            "ReadClientCredentialsGrantDetails.token_endpoint required"
        )
    return out
