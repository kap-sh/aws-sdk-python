"""Generated from Smithy shape ``com.amazonaws.glue#ComputationType``."""

from typing import Literal, TypeAlias, cast

ComputationType: TypeAlias = Literal[
    "FULL",
    "INCREMENTAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComputationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ComputationType:
    return cast(ComputationType, data)
