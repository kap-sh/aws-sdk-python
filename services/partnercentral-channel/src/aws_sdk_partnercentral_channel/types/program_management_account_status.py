"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountStatus``."""

from typing import Literal, TypeAlias, cast

ProgramManagementAccountStatus: TypeAlias = Literal[
    "PENDING",
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProgramManagementAccountStatus:
    return cast(ProgramManagementAccountStatus, data)
