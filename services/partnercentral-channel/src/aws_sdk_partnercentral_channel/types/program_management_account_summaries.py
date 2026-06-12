"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#ProgramManagementAccountSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_partnercentral_channel.types.program_management_account_summary

ProgramManagementAccountSummaries: TypeAlias = list[
    "aws_sdk_partnercentral_channel.types.program_management_account_summary.ProgramManagementAccountSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProgramManagementAccountSummaries) -> list:
    import aws_sdk_partnercentral_channel.types.program_management_account_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_partnercentral_channel.types.program_management_account_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ProgramManagementAccountSummaries:
    import aws_sdk_partnercentral_channel.types.program_management_account_summary

    out: ProgramManagementAccountSummaries = []
    for item in data:
        out.append(
            aws_sdk_partnercentral_channel.types.program_management_account_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
