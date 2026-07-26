"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionFeatureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rekognition.types.label_detection_feature_name

LabelDetectionFeatureList: TypeAlias = list[
    "capo_rekognition.types.label_detection_feature_name.LabelDetectionFeatureName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelDetectionFeatureList) -> list:
    import capo_rekognition.types.label_detection_feature_name

    out: list = []
    for item in value:
        out.append(
            capo_rekognition.types.label_detection_feature_name.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LabelDetectionFeatureList:
    import capo_rekognition.types.label_detection_feature_name

    out: LabelDetectionFeatureList = []
    for item in data:
        out.append(
            capo_rekognition.types.label_detection_feature_name.deserialize_aws_json_1_1(
                item
            )
        )
    return out
