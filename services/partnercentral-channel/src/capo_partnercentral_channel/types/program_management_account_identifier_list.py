"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_partnercentral_channel.types.program_management_account_identifier

ProgramManagementAccountIdentifierList: TypeAlias = list[
    "capo_partnercentral_channel.types.program_management_account_identifier.ProgramManagementAccountIdentifier"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountIdentifierList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> ProgramManagementAccountIdentifierList:
    return list(data)
