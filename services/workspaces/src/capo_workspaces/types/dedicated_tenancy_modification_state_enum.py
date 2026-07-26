"""Generated from Smithy shape ``com.amazonaws.workspaces#DedicatedTenancyModificationStateEnum``."""

from typing import Literal, TypeAlias, cast

DedicatedTenancyModificationStateEnum: TypeAlias = Literal[
    "PENDING",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DedicatedTenancyModificationStateEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DedicatedTenancyModificationStateEnum:
    return cast(DedicatedTenancyModificationStateEnum, data)
