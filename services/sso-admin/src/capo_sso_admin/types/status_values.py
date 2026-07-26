"""Generated from Smithy shape ``com.amazonaws.ssoadmin#StatusValues``."""

from typing import Literal, TypeAlias, cast

StatusValues: TypeAlias = Literal[
    "IN_PROGRESS",
    "FAILED",
    "SUCCEEDED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StatusValues) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> StatusValues:
    return cast(StatusValues, data)
