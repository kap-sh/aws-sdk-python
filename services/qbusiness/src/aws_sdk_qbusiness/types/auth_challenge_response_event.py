"""Generated from Smithy shape ``com.amazonaws.qbusiness#AuthChallengeResponseEvent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qbusiness._protocol.eventstream import HeaderValue, Message
from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.authorization_response_map


class AuthChallengeResponseEvent(TypedDict, closed=True):
    response_map: (
        "aws_sdk_qbusiness.types.authorization_response_map.AuthorizationResponseMap"
    )
    """<p>The mapping of key-value pairs in an authentication challenge response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthChallengeResponseEvent) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.authorization_response_map

    out["responseMap"] = (
        aws_sdk_qbusiness.types.authorization_response_map.serialize_json(
            value["response_map"]
        )
    )
    return out


def deserialize_json(data: dict) -> AuthChallengeResponseEvent:
    out: AuthChallengeResponseEvent = {}  # type: ignore[typeddict-item]
    if "responseMap" in data:
        import aws_sdk_qbusiness.types.authorization_response_map

        out["response_map"] = (
            aws_sdk_qbusiness.types.authorization_response_map.deserialize_json(
                data["responseMap"]
            )
        )
    else:
        raise DeserializationError("AuthChallengeResponseEvent.response_map required")
    return out


def serialize_event_json(value: AuthChallengeResponseEvent) -> bytes:
    headers: dict[str, HeaderValue] = {":event-type": "authChallengeResponseEvent"}
    payload = b""
    return Message(headers=headers, payload=payload).encode()


def deserialize_event_json(message: Message) -> AuthChallengeResponseEvent:
    headers = message.headers  # noqa: F841
    payload = message.payload  # noqa: F841
    out: AuthChallengeResponseEvent = {}  # type: ignore[typeddict-item]
    return out
