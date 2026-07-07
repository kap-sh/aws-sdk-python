"""Generated from Smithy shape ``com.amazonaws.quicksight#ClientCredentialsGrantDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.client_id
    import aws_sdk_quicksight.types.client_secret
    import aws_sdk_quicksight.types.endpoint


class ClientCredentialsGrantDetails(TypedDict, closed=True):
    client_id: "aws_sdk_quicksight.types.client_id.ClientId"
    """<p>The client identifier issued to the client during the registration process with the authorization server.</p>"""
    client_secret: "aws_sdk_quicksight.types.client_secret.ClientSecret"
    """<p>The client secret issued to the client during the registration process with the authorization server.</p>"""
    token_endpoint: "aws_sdk_quicksight.types.endpoint.Endpoint"
    """<p>The authorization server endpoint used to obtain access tokens via the client credentials grant flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClientCredentialsGrantDetails) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["ClientSecret"] = value["client_secret"]
    out["TokenEndpoint"] = value["token_endpoint"]
    return out


def deserialize_json(data: dict) -> ClientCredentialsGrantDetails:
    out: ClientCredentialsGrantDetails = {}  # type: ignore[typeddict-item]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("ClientCredentialsGrantDetails.client_id required")
    if "ClientSecret" in data:
        out["client_secret"] = data["ClientSecret"]
    else:
        raise DeserializationError(
            "ClientCredentialsGrantDetails.client_secret required"
        )
    if "TokenEndpoint" in data:
        out["token_endpoint"] = data["TokenEndpoint"]
    else:
        raise DeserializationError(
            "ClientCredentialsGrantDetails.token_endpoint required"
        )
    return out
