"""Generated from Smithy shape ``com.amazonaws.glue#ExistCondition``."""

from typing import Literal, TypeAlias, cast

ExistCondition: TypeAlias = Literal[
    "MUST_EXIST",
    "NOT_EXIST",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExistCondition) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExistCondition:
    return cast(ExistCondition, data)
