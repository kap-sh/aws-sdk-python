"""Generated from Smithy shape ``com.amazonaws.backup#GetLegalHoldInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string


class GetLegalHoldInput(TypedDict, closed=True):
    legal_hold_id: "capo_backup.types.string.string"
    """<p>The ID of the legal hold.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetLegalHoldInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetLegalHoldInput:
    out: GetLegalHoldInput = {}  # type: ignore[typeddict-item]
    return out
