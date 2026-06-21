"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountTypeSortName``."""

from typing import Literal, TypeAlias, cast

ProgramManagementAccountTypeSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountTypeSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProgramManagementAccountTypeSortName:
    return cast(ProgramManagementAccountTypeSortName, data)
