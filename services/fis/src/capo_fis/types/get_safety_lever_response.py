"""Generated from Smithy shape ``com.amazonaws.fis#GetSafetyLeverResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.safety_lever


class GetSafetyLeverResponse(TypedDict, closed=True):
    safety_lever: NotRequired["capo_fis.types.safety_lever.SafetyLever"]
    """<p> Information about the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSafetyLeverResponse) -> dict:
    out: dict = {}
    if "safety_lever" in value:
        import capo_fis.types.safety_lever

        out["safetyLever"] = capo_fis.types.safety_lever.serialize_json(
            value["safety_lever"]
        )
    return out


def deserialize_json(data: dict) -> GetSafetyLeverResponse:
    out: GetSafetyLeverResponse = {}  # type: ignore[typeddict-item]
    if "safetyLever" in data:
        import capo_fis.types.safety_lever

        out["safety_lever"] = capo_fis.types.safety_lever.deserialize_json(
            data["safetyLever"]
        )
    return out
