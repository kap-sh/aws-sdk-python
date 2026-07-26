"""Generated from Smithy shape ``com.amazonaws.sagemaker#AwsManagedHumanLoopRequestSource``."""

from typing import Literal, TypeAlias, cast

AwsManagedHumanLoopRequestSource: TypeAlias = Literal[
    "AWS/Rekognition/DetectModerationLabels/Image/V3",
    "AWS/Textract/AnalyzeDocument/Forms/V1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AwsManagedHumanLoopRequestSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AwsManagedHumanLoopRequestSource:
    return cast(AwsManagedHumanLoopRequestSource, data)
