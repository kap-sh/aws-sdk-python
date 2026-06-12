"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_qbusiness.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.url

class AuthChallengeRequest(TypedDict):
    authorization_url: "aws_sdk_qbusiness.types.url.Url"
    """<p>The URL sent by Amazon Q Business to the third party authentication server to authenticate a custom plugin user through an OAuth protocol.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeRequest) -> dict:
    out: dict = {}
    out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> AuthChallengeRequest:
    out: AuthChallengeRequest = {}  # type: ignore[typeddict-item]
    if "authorizationUrl" in data:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        raise DeserializationError("AuthChallengeRequest.authorization_url required")
    return out