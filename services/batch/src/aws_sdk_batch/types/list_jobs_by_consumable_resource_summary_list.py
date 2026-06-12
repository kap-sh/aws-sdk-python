"""Generated from Smithy shape ``com.amazonaws.batch#ListJobsByConsumableResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.list_jobs_by_consumable_resource_summary

ListJobsByConsumableResourceSummaryList: TypeAlias = list[
    "aws_sdk_batch.types.list_jobs_by_consumable_resource_summary.ListJobsByConsumableResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ListJobsByConsumableResourceSummaryList) -> list:
    import aws_sdk_batch.types.list_jobs_by_consumable_resource_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_batch.types.list_jobs_by_consumable_resource_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ListJobsByConsumableResourceSummaryList:
    import aws_sdk_batch.types.list_jobs_by_consumable_resource_summary

    out: ListJobsByConsumableResourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.list_jobs_by_consumable_resource_summary.deserialize_json(
                item
            )
        )
    return out
