"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecordWrapper``."""

from typing import Literal, TypeAlias, cast

RecordWrapper: TypeAlias = Literal[
    "None",
    "RecordIO",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecordWrapper) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RecordWrapper:
    return cast(RecordWrapper, data)
