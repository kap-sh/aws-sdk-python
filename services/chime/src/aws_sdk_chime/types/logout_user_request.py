"""Generated from Smithy shape ``com.amazonaws.chime#LogoutUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class LogoutUserRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LogoutUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> LogoutUserRequest:
    out: LogoutUserRequest = {}  # type: ignore[typeddict-item]
    return out
