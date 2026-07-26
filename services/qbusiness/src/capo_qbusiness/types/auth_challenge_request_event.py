"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeRequestEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qbusiness._protocol.eventstream import HeaderValue, Message
from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.url


class AuthChallengeRequestEvent(TypedDict, closed=True):
    authorization_url: "capo_qbusiness.types.url.Url"
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


def serialize_event_json(value: AuthChallengeRequestEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "authChallengeRequestEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AuthChallengeRequestEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AuthChallengeRequestEvent = {}  # type: ignore[typeddict-item]
    return out
