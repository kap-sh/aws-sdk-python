"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_management_account_status

ProgramManagementAccountStatusList: TypeAlias = list[
    "capo_partnercentral_channel.types.program_management_account_status.ProgramManagementAccountStatus"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountStatusList) -> list:
    import capo_partnercentral_channel.types.program_management_account_status

    out: list = []
    for item in value:
        out.append(
            capo_partnercentral_channel.types.program_management_account_status.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProgramManagementAccountStatusList:
    import capo_partnercentral_channel.types.program_management_account_status

    out: ProgramManagementAccountStatusList = []
    for item in data:
        out.append(
            capo_partnercentral_channel.types.program_management_account_status.deserialize_aws_json_1_0(
                item
            )
        )
    return out
