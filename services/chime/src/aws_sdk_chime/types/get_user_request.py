"""Generated from Smithy shape ``com.amazonaws.chime#GetUserRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class GetUserRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetUserRequest:
    out: GetUserRequest = {}  # type: ignore[typeddict-item]
    return out
