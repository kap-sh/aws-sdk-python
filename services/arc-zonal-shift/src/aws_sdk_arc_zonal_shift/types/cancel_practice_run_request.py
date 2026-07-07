"""Generated from Smithy shape ``com.amazonaws.arczonalshift#CancelPracticeRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_arc_zonal_shift.types.zonal_shift_id


class CancelPracticeRunRequest(TypedDict, closed=True):
    zonal_shift_id: "aws_sdk_arc_zonal_shift.types.zonal_shift_id.ZonalShiftId"
    """<p>The identifier of a practice run zonal shift in Amazon Application Recovery Controller that you want to cancel.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelPracticeRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelPracticeRunRequest:
    out: CancelPracticeRunRequest = {}  # type: ignore[typeddict-item]
    return out
