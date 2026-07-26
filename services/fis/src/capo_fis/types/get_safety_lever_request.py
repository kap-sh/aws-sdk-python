"""Generated from Smithy shape ``com.amazonaws.fis#GetSafetyLeverRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fis.types.safety_lever_id


class GetSafetyLeverRequest(TypedDict, closed=True):
    id: "capo_fis.types.safety_lever_id.SafetyLeverId"
    """<p> The ID of the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSafetyLeverRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSafetyLeverRequest:
    out: GetSafetyLeverRequest = {}  # type: ignore[typeddict-item]
    return out
