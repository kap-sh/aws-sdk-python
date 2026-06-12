"""Generated from Smithy shape ``com.amazonaws.apprunner#OperationSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.operation_summary

OperationSummaryList: TypeAlias = list[
    "aws_sdk_apprunner.types.operation_summary.OperationSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OperationSummaryList) -> list:
    import aws_sdk_apprunner.types.operation_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_apprunner.types.operation_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> OperationSummaryList:
    import aws_sdk_apprunner.types.operation_summary

    out: OperationSummaryList = []
    for item in data:
        out.append(
            aws_sdk_apprunner.types.operation_summary.deserialize_aws_json_1_0(item)
        )
    return out
