"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceCurrentRevisionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_current_revision_summary

ServiceCurrentRevisionSummaryList: TypeAlias = list[
    "aws_sdk_ecs.types.service_current_revision_summary.ServiceCurrentRevisionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceCurrentRevisionSummaryList) -> list:
    import aws_sdk_ecs.types.service_current_revision_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.service_current_revision_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceCurrentRevisionSummaryList:
    import aws_sdk_ecs.types.service_current_revision_summary

    out: ServiceCurrentRevisionSummaryList = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.service_current_revision_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
