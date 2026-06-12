"""Generated from Smithy shape ``com.amazonaws.resourcegroupstaggingapi#SummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resource_groups_tagging_api.types.summary

SummaryList: TypeAlias = list[
    "aws_sdk_resource_groups_tagging_api.types.summary.Summary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummaryList) -> list:
    import aws_sdk_resource_groups_tagging_api.types.summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SummaryList:
    import aws_sdk_resource_groups_tagging_api.types.summary

    out: SummaryList = []
    for item in data:
        out.append(
            aws_sdk_resource_groups_tagging_api.types.summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
