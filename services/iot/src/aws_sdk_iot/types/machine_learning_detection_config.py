"""Generated from Smithy shape ``com.amazonaws.iot#MachineLearningDetectionConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.confidence_level


class MachineLearningDetectionConfig(TypedDict, closed=True):
    confidence_level: "aws_sdk_iot.types.confidence_level.ConfidenceLevel"
    """<p> The sensitivity of anomalous behavior evaluation. Can be <code>Low</code>, <code>Medium</code>, or <code>High</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MachineLearningDetectionConfig) -> dict:
    out: dict = {}
    import aws_sdk_iot.types.confidence_level

    out["confidenceLevel"] = aws_sdk_iot.types.confidence_level.serialize_json(
        value["confidence_level"]
    )
    return out


def deserialize_json(data: dict) -> MachineLearningDetectionConfig:
    out: MachineLearningDetectionConfig = {}  # type: ignore[typeddict-item]
    if "confidenceLevel" in data:
        import aws_sdk_iot.types.confidence_level

        out["confidence_level"] = aws_sdk_iot.types.confidence_level.deserialize_json(
            data["confidenceLevel"]
        )
    else:
        raise DeserializationError(
            "MachineLearningDetectionConfig.confidence_level required"
        )
    return out
