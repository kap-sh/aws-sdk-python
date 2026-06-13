"""Generated from Smithy shape ``com.amazonaws.backup#CancelLegalHoldInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_backup.types.long
    import aws_sdk_backup.types.string


class CancelLegalHoldInput(TypedDict):
    legal_hold_id: "aws_sdk_backup.types.string.string"
    """<p>The ID of the legal hold.</p>"""
    cancel_description: "aws_sdk_backup.types.string.string"
    """<p>A string the describes the reason for removing the legal hold.</p>"""
    retain_record_in_days: NotRequired["aws_sdk_backup.types.long.Long"]
    """<p>The integer amount, in days, after which to remove legal hold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelLegalHoldInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelLegalHoldInput:
    out: CancelLegalHoldInput = {}  # type: ignore[typeddict-item]
    return out
