"""Generated from Smithy shape ``com.amazonaws.sagemaker#LastUpdateStatusValue``."""

from typing import Literal, TypeAlias, cast

LastUpdateStatusValue: TypeAlias = Literal[
    "Successful",
    "Failed",
    "InProgress",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LastUpdateStatusValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LastUpdateStatusValue:
    return cast(LastUpdateStatusValue, data)
