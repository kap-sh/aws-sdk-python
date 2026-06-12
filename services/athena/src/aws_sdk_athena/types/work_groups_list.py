"""Generated from Smithy shape ``com.amazonaws.athena#WorkGroupsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_athena.types.work_group_summary

WorkGroupsList: TypeAlias = list[
    "aws_sdk_athena.types.work_group_summary.WorkGroupSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkGroupsList) -> list:
    import aws_sdk_athena.types.work_group_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_athena.types.work_group_summary.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> WorkGroupsList:
    import aws_sdk_athena.types.work_group_summary

    out: WorkGroupsList = []
    for item in data:
        out.append(
            aws_sdk_athena.types.work_group_summary.deserialize_aws_json_1_1(item)
        )
    return out
