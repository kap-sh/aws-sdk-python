"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeRequestEvent``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.url


class AuthChallengeRequestEvent(TypedDict):
    authorization_url: "aws_sdk_qbusiness.types.url.Url"
    """<p>The URL sent by Amazon Q Business to a third party authentication server in response to an authentication verification event activated by an end user request to use a custom plugin. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeRequestEvent) -> dict:
    out: dict = {}
    out["authorizationUrl"] = value["authorization_url"]
    return out


def deserialize_json(data: dict) -> AuthChallengeRequestEvent:
    out: AuthChallengeRequestEvent = {}  # type: ignore[typeddict-item]
    if "authorizationUrl" in data:
        out["authorization_url"] = data["authorizationUrl"]
    else:
        raise DeserializationError(
            "AuthChallengeRequestEvent.authorization_url required"
        )
    return out
