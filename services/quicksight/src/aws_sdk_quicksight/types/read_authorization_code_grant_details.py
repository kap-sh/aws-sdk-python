"""Generated from Smithy shape ``com.amazonaws.quicksight#ReadAuthorizationCodeGrantDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.client_id
    import aws_sdk_quicksight.types.endpoint


class ReadAuthorizationCodeGrantDetails(TypedDict, closed=True):
    client_id: "aws_sdk_quicksight.types.client_id.ClientId"
    """<p>The client identifier for the OAuth2 authorization code grant flow.</p>"""
    token_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The authorization server endpoint used to obtain access tokens via the authorization code grant flow.</p>"""
    authorization_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The authorization server endpoint used to obtain authorization codes from the resource owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadAuthorizationCodeGrantDetails) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["TokenEndpoint"] = value["token_endpoint"]
    out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    return out


def deserialize_json(data: dict) -> ReadAuthorizationCodeGrantDetails:
    out: ReadAuthorizationCodeGrantDetails = {}  # type: ignore[typeddict-item]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError(
            "ReadAuthorizationCodeGrantDetails.client_id required"
        )
    if "TokenEndpoint" in data:
        out["token_endpoint"] = data["TokenEndpoint"]
    else:
        raise DeserializationError(
            "ReadAuthorizationCodeGrantDetails.token_endpoint required"
        )
    if "AuthorizationEndpoint" in data:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    else:
        raise DeserializationError(
            "ReadAuthorizationCodeGrantDetails.authorization_endpoint required"
        )
    return out
