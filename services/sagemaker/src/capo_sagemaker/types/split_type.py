"""Generated from Smithy shape ``com.amazonaws.sagemaker#SplitType``."""

from typing import Literal, TypeAlias, cast

SplitType: TypeAlias = Literal[
    "None",
    "Line",
    "RecordIO",
    "TFRecord",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SplitType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SplitType:
    return cast(SplitType, data)
