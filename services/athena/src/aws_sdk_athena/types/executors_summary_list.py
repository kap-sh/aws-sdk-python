"""Generated from Smithy shape ``com.amazonaws.athena#ExecutorsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.executors_summary

ExecutorsSummaryList: TypeAlias = list[
    "aws_sdk_athena.types.executors_summary.ExecutorsSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutorsSummaryList) -> list:
    import aws_sdk_athena.types.executors_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.executors_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ExecutorsSummaryList:
    import aws_sdk_athena.types.executors_summary

    out: ExecutorsSummaryList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.executors_summary.deserialize_aws_json_1_1(item)
        )
    return out
