"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionRedriveFilter``."""

from typing import Literal, TypeAlias, cast

ExecutionRedriveFilter: TypeAlias = Literal[
    "REDRIVEN",
    "NOT_REDRIVEN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionRedriveFilter) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionRedriveFilter:
    return cast(ExecutionRedriveFilter, data)
