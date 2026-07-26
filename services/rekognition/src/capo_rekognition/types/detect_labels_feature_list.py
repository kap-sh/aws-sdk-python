"""Generated from Smithy shape ``com.amazonaws.rekognition#DetectLabelsFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.detect_labels_feature_name

DetectLabelsFeatureList: TypeAlias = list[
    "capo_rekognition.types.detect_labels_feature_name.DetectLabelsFeatureName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectLabelsFeatureList) -> list:
    import capo_rekognition.types.detect_labels_feature_name

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.detect_labels_feature_name.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DetectLabelsFeatureList:
    import capo_rekognition.types.detect_labels_feature_name

    out: DetectLabelsFeatureList = []
    for item in data:
        out.append(
            capo_rekognition.types.detect_labels_feature_name.deserialize_aws_json_1_1(
                item
            )
        )
    return out
