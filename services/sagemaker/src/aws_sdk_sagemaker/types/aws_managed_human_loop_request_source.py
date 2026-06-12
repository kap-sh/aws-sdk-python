"""Generated from Smithy shape ``com.amazonaws.sagemaker#AwsManagedHumanLoopRequestSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

AwsManagedHumanLoopRequestSource: TypeAlias = Literal[
    "AWS/Rekognition/DetectModerationLabels/Image/V3",
    "AWS/Textract/AnalyzeDocument/Forms/V1",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS/Rekognition/DetectModerationLabels/Image/V3",
        "AWS/Textract/AnalyzeDocument/Forms/V1",
    )
)


def serialize_aws_json_1_1(value: AwsManagedHumanLoopRequestSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AwsManagedHumanLoopRequestSource:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AwsManagedHumanLoopRequestSource value: {data!r}"
        )
    return cast(AwsManagedHumanLoopRequestSource, data)
