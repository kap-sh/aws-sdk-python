"""Generated from Smithy shape ``com.amazonaws.connectparticipant#GetAuthenticationUrlResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectparticipant.types.authentication_url


class GetAuthenticationUrlResponse(TypedDict, closed=True):
    authentication_url: NotRequired[
        "capo_connectparticipant.types.authentication_url.AuthenticationUrl"
    ]
    """<p>The URL where the customer will sign in to the identity provider. This URL contains the authorize endpoint for the Cognito UserPool used in the authentication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAuthenticationUrlResponse) -> dict:
    out: dict = {}
    if "authentication_url" in value:
        out["AuthenticationUrl"] = value["authentication_url"]
    return out


def deserialize_json(data: dict) -> GetAuthenticationUrlResponse:
    out: GetAuthenticationUrlResponse = {}  # type: ignore[typeddict-item]
    if "AuthenticationUrl" in data:
        out["authentication_url"] = data["AuthenticationUrl"]
    return out
