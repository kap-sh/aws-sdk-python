"""Generated from Smithy shape ``com.amazonaws.ivschat#CreateChatTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivschat.types.chat_token
    import aws_sdk_ivschat.types.time


class CreateChatTokenResponse(TypedDict, closed=True):
    token: NotRequired["aws_sdk_ivschat.types.chat_token.ChatToken"]
    """<p>The issued client token, encrypted.</p>"""
    token_expiration_time: NotRequired["aws_sdk_ivschat.types.time.Time"]
    """<p>Time after which the token is no longer valid and cannot be used to connect to a room. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""
    session_expiration_time: NotRequired["aws_sdk_ivschat.types.time.Time"]
    """<p>Time after which an end user's session is no longer valid. This is an ISO 8601 timestamp; <i>note that this is returned as a string</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChatTokenResponse) -> dict:
    out: dict = {}
    if "token" in value:
        out["token"] = value["token"]
    if "token_expiration_time" in value:
        import aws_sdk_ivschat.types.time

        out["tokenExpirationTime"] = aws_sdk_ivschat.types.time.serialize_json(
            value["token_expiration_time"]
        )
    if "session_expiration_time" in value:
        import aws_sdk_ivschat.types.time

        out["sessionExpirationTime"] = aws_sdk_ivschat.types.time.serialize_json(
            value["session_expiration_time"]
        )
    return out


def deserialize_json(data: dict) -> CreateChatTokenResponse:
    out: CreateChatTokenResponse = {}  # type: ignore[typeddict-item]
    if "token" in data:
        out["token"] = data["token"]
    if "tokenExpirationTime" in data:
        import aws_sdk_ivschat.types.time

        out["token_expiration_time"] = aws_sdk_ivschat.types.time.deserialize_json(
            data["tokenExpirationTime"]
        )
    if "sessionExpirationTime" in data:
        import aws_sdk_ivschat.types.time

        out["session_expiration_time"] = aws_sdk_ivschat.types.time.deserialize_json(
            data["sessionExpirationTime"]
        )
    return out
