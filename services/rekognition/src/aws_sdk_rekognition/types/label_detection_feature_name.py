"""Generated from Smithy shape ``com.amazonaws.rekognition#LabelDetectionFeatureName``."""

from typing import Literal, TypeAlias, cast

LabelDetectionFeatureName: TypeAlias = Literal["GENERAL_LABELS",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LabelDetectionFeatureName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LabelDetectionFeatureName:
    return cast(LabelDetectionFeatureName, data)
