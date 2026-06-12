"""Generated from Smithy shape ``com.amazonaws.apprunner#ConnectionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_apprunner.types.connection_summary

ConnectionSummaryList: TypeAlias = list[
    "aws_sdk_apprunner.types.connection_summary.ConnectionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ConnectionSummaryList) -> list:
    import aws_sdk_apprunner.types.connection_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_apprunner.types.connection_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ConnectionSummaryList:
    import aws_sdk_apprunner.types.connection_summary

    out: ConnectionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_apprunner.types.connection_summary.deserialize_aws_json_1_0(item)
        )
    return out
