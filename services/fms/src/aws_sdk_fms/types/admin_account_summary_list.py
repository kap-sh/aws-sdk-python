"""Generated from Smithy shape ``com.amazonaws.fms#AdminAccountSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fms.types.admin_account_summary

AdminAccountSummaryList: TypeAlias = list[
    "aws_sdk_fms.types.admin_account_summary.AdminAccountSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdminAccountSummaryList) -> list:
    import aws_sdk_fms.types.admin_account_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_fms.types.admin_account_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> AdminAccountSummaryList:
    import aws_sdk_fms.types.admin_account_summary

    out: AdminAccountSummaryList = []
    for item in data:
        out.append(
            aws_sdk_fms.types.admin_account_summary.deserialize_aws_json_1_1(item)
        )
    return out
