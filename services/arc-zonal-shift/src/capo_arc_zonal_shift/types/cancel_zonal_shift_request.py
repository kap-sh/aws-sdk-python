"""Generated from Smithy shape ``com.amazonaws.arczonalshift#CancelZonalShiftRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_arc_zonal_shift.types.zonal_shift_id


class CancelZonalShiftRequest(TypedDict, closed=True):
    zonal_shift_id: "capo_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId"
    """<p>The internally-generated identifier of a zonal shift.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelZonalShiftRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelZonalShiftRequest:
    out: CancelZonalShiftRequest = {}  # type: ignore[typeddict-item]
    return out
