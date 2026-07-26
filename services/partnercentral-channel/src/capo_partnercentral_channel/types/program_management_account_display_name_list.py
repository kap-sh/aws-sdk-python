"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountDisplayNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_management_account_display_name

ProgramManagementAccountDisplayNameList: TypeAlias = list[
    "capo_partnercentral_channel.types.program_management_account_display_name.ProgramManagementAccountDisplayName"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountDisplayNameList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProgramManagementAccountDisplayNameList:
    return list(data)
