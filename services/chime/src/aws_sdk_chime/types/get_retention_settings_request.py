"""Generated from Smithy shape ``com.amazonaws.chime#GetRetentionSettingsRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class GetRetentionSettingsRequest(TypedDict):
    account_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The Amazon Chime account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRetentionSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRetentionSettingsRequest:
    out: GetRetentionSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
