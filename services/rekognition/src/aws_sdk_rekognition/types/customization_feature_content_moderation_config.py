"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomizationFeatureContentModerationConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.percent


class CustomizationFeatureContentModerationConfig(TypedDict):
    confidence_threshold: NotRequired["aws_sdk_rekognition.types.percent.Percent"]
    """<p>The confidence level you plan to use to identify if unsafe content is present during inference.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizationFeatureContentModerationConfig) -> dict:
    out: dict = {}
    if "confidence_threshold" in value:
        out["ConfidenceThreshold"] = value["confidence_threshold"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomizationFeatureContentModerationConfig:
    out: CustomizationFeatureContentModerationConfig = {}  # type: ignore[typeddict-item]
    if "ConfidenceThreshold" in data:
        out["confidence_threshold"] = data["ConfidenceThreshold"]
    return out
