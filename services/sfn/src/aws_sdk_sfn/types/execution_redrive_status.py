"""Generated from Smithy shape ``com.amazonaws.sfn#ExecutionRedriveStatus``."""

from typing import Literal, TypeAlias, cast

ExecutionRedriveStatus: TypeAlias = Literal[
    "REDRIVABLE",
    "NOT_REDRIVABLE",
    "REDRIVABLE_BY_MAP_RUN",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExecutionRedriveStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ExecutionRedriveStatus:
    return cast(ExecutionRedriveStatus, data)
