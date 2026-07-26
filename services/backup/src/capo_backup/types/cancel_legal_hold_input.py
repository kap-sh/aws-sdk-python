"""Generated from Smithy shape ``com.amazonaws.backup#CancelLegalHoldInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.long
    import capo_backup.types.string


class CancelLegalHoldInput(TypedDict, closed=True):
    legal_hold_id: "capo_backup.types.string.string"
    """<p>The ID of the legal hold.</p>"""
    cancel_description: "capo_backup.types.string.string"
    """<p>A string the describes the reason for removing the legal hold.</p>"""
    retain_record_in_days: NotRequired["capo_backup.types.long.Long"]
    """<p>The integer amount, in days, after which to remove legal hold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelLegalHoldInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelLegalHoldInput:
    out: CancelLegalHoldInput = {}  # type: ignore[typeddict-item]
    return out
