"""Generated from Smithy shape ``com.amazonaws.fis#UpdateSafetyLeverStateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fis.types.safety_lever


class UpdateSafetyLeverStateResponse(TypedDict):
    safety_lever: NotRequired["aws_sdk_fis.types.safety_lever.SafetyLever"]
    """<p> Information about the safety lever. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSafetyLeverStateResponse) -> dict:
    out: dict = {}
    if "safety_lever" in value:
        import aws_sdk_fis.types.safety_lever

        out["safetyLever"] = aws_sdk_fis.types.safety_lever.serialize_json(
            value["safety_lever"]
        )
    return out


def deserialize_json(data: dict) -> UpdateSafetyLeverStateResponse:
    out: UpdateSafetyLeverStateResponse = {}  # type: ignore[typeddict-item]
    if "safetyLever" in data:
        import aws_sdk_fis.types.safety_lever

        out["safety_lever"] = aws_sdk_fis.types.safety_lever.deserialize_json(
            data["safetyLever"]
        )
    return out
