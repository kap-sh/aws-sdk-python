"""Generated from Smithy shape ``com.amazonaws.iot#ViolationEventAdditionalInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.confidence_level


class ViolationEventAdditionalInfo(TypedDict, closed=True):
    confidence_level: NotRequired["capo_iot.types.confidence_level.ConfidenceLevel"]
    """<p> The sensitivity of anomalous behavior evaluation. Can be <code>Low</code>, <code>Medium</code>, or <code>High</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ViolationEventAdditionalInfo) -> dict:
    out: dict = {}
    if "confidence_level" in value:
        import capo_iot.types.confidence_level

        out["confidenceLevel"] = capo_iot.types.confidence_level.serialize_json(
            value["confidence_level"]
        )
    return out


def deserialize_json(data: dict) -> ViolationEventAdditionalInfo:
    out: ViolationEventAdditionalInfo = {}  # type: ignore[typeddict-item]
    if "confidenceLevel" in data:
        import capo_iot.types.confidence_level

        out["confidence_level"] = capo_iot.types.confidence_level.deserialize_json(
            data["confidenceLevel"]
        )
    return out
