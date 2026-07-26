"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomizationFeature``."""

from typing import Literal, TypeAlias, cast

CustomizationFeature: TypeAlias = Literal[
    "CONTENT_MODERATION",
    "CUSTOM_LABELS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizationFeature) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomizationFeature:
    return cast(CustomizationFeature, data)
