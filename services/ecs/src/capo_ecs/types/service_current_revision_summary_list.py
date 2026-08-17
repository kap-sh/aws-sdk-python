"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceCurrentRevisionSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_current_revision_summary

ServiceCurrentRevisionSummaryList: TypeAlias = list[
    "capo_ecs.types.service_current_revision_summary.ServiceCurrentRevisionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceCurrentRevisionSummaryList) -> list:
    import capo_ecs.types.service_current_revision_summary

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.service_current_revision_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceCurrentRevisionSummaryList:
    import capo_ecs.types.service_current_revision_summary

    out: ServiceCurrentRevisionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.service_current_revision_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
