"""Generated from Smithy shape ``com.amazonaws.ssm#StopType``."""

from typing import Literal, TypeAlias, cast

StopType: TypeAlias = Literal[
    "Complete",
    "Cancel",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StopType:
    return cast(StopType, data)
