"""Generated from Smithy shape ``com.amazonaws.cognitosync#GetCognitoEventsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cognito_sync.types.identity_pool_id


class GetCognitoEventsRequest(TypedDict, closed=True):
    identity_pool_id: "capo_cognito_sync.types.identity_pool_id.IdentityPoolId"
    """<p>The Cognito Identity Pool ID for the request</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCognitoEventsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCognitoEventsRequest:
    out: GetCognitoEventsRequest = {}  # type: ignore[typeddict-item]
    return out
