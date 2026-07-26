"""Generated from Smithy shape ``com.amazonaws.amplifybackend#GetTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string


class GetTokenResponse(TypedDict, closed=True):
    app_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The app ID.</p>"""
    challenge_code: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The one-time challenge code for authenticating into the Amplify Admin UI.</p>"""
    session_id: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>A unique ID provided when creating a new challenge token.</p>"""
    ttl: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The expiry time for the one-time generated token code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenResponse) -> dict:
    out: dict = {}
    if "app_id" in value:
        out["appId"] = value["app_id"]
    if "challenge_code" in value:
        out["challengeCode"] = value["challenge_code"]
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "ttl" in value:
        out["ttl"] = value["ttl"]
    return out


def deserialize_json(data: dict) -> GetTokenResponse:
    out: GetTokenResponse = {}  # type: ignore[typeddict-item]
    if "appId" in data:
        out["app_id"] = data["appId"]
    if "challengeCode" in data:
        out["challenge_code"] = data["challengeCode"]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "ttl" in data:
        out["ttl"] = data["ttl"]
    return out
