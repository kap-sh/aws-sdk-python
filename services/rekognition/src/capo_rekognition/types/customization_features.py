"""Generated from Smithy shape ``com.amazonaws.rekognition#CustomizationFeatures``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.customization_feature

CustomizationFeatures: TypeAlias = list[
    "capo_rekognition.types.customization_feature.CustomizationFeature"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomizationFeatures) -> list:
    import capo_rekognition.types.customization_feature

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.customization_feature.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomizationFeatures:
    import capo_rekognition.types.customization_feature

    out: CustomizationFeatures = []
    for item in data:
        out.append(
            capo_rekognition.types.customization_feature.deserialize_aws_json_1_1(item)
        )
    return out
