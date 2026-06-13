"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentAccountConnectionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_proton.types.environment_account_connection_summary

EnvironmentAccountConnectionSummaryList: TypeAlias = list[
    "aws_sdk_proton.types.environment_account_connection_summary.EnvironmentAccountConnectionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentAccountConnectionSummaryList) -> list:
    import aws_sdk_proton.types.environment_account_connection_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_proton.types.environment_account_connection_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EnvironmentAccountConnectionSummaryList:
    import aws_sdk_proton.types.environment_account_connection_summary

    out: EnvironmentAccountConnectionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_proton.types.environment_account_connection_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
