"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsFeatureName``."""

from typing import Literal, TypeAlias, cast

DetectLabelsFeatureName: TypeAlias = Literal[
    "GENERAL_LABELS",
    "IMAGE_PROPERTIES",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsFeatureName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DetectLabelsFeatureName:
    return cast(DetectLabelsFeatureName, data)
