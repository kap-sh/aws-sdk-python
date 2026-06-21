"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ListProgramManagementAccountsSortName``."""

from typing import Literal, TypeAlias, cast

ListProgramManagementAccountsSortName: TypeAlias = Literal["UpdatedAt",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListProgramManagementAccountsSortName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ListProgramManagementAccountsSortName:
    return cast(ListProgramManagementAccountsSortName, data)
