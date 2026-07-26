"""Generated from Smithy shape ``com.amazonaws.quicksight#AuthorizationCodeGrantDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.client_id
    import capo_quicksight.types.client_secret
    import capo_quicksight.types.endpoint


class AuthorizationCodeGrantDetails(TypedDict, closed=True):
    client_id: "capo_quicksight.types.client_id.ClientId"
    """<p>The client ID for the OAuth application.</p>"""
    client_secret: "capo_quicksight.types.client_secret.ClientSecret"
    """<p>The client secret for the OAuth application.</p>"""
    token_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The token endpoint URL for obtaining access tokens.</p>"""
    authorization_endpoint: "capo_quicksight.types.endpoint.Endpoint"
    """<p>The authorization endpoint URL for the OAuth flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthorizationCodeGrantDetails) -> dict:
    out: dict = {}
    out["ClientId"] = value["client_id"]
    out["ClientSecret"] = value["client_secret"]
    out["TokenEndpoint"] = value["token_endpoint"]
    out["AuthorizationEndpoint"] = value["authorization_endpoint"]
    return out


def deserialize_json(data: dict) -> AuthorizationCodeGrantDetails:
    out: AuthorizationCodeGrantDetails = {}  # type: ignore[typeddict-item]
    if "ClientId" in data:
        out["client_id"] = data["ClientId"]
    else:
        raise DeserializationError("AuthorizationCodeGrantDetails.client_id required")
    if "ClientSecret" in data:
        out["client_secret"] = data["ClientSecret"]
    else:
        raise DeserializationError(
            "AuthorizationCodeGrantDetails.client_secret required"
        )
    if "TokenEndpoint" in data:
        out["token_endpoint"] = data["TokenEndpoint"]
    else:
        raise DeserializationError(
            "AuthorizationCodeGrantDetails.token_endpoint required"
        )
    if "AuthorizationEndpoint" in data:
        out["authorization_endpoint"] = data["AuthorizationEndpoint"]
    else:
        raise DeserializationError(
            "AuthorizationCodeGrantDetails.authorization_endpoint required"
        )
    return out
