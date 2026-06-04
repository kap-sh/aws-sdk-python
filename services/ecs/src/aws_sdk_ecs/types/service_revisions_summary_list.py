"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionsSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_revision_summary

ServiceRevisionsSummaryList: TypeAlias = list[
    "aws_sdk_ecs.types.service_revision_summary.ServiceRevisionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisionsSummaryList) -> list:
    import aws_sdk_ecs.types.service_revision_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.service_revision_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceRevisionsSummaryList:
    import aws_sdk_ecs.types.service_revision_summary

    out: ServiceRevisionsSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.service_revision_summary.deserialize_aws_json_1_1(item)
        )
    return out
