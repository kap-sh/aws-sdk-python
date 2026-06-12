"""Generated from Smithy shape ``com.amazonaws.batch#ConsumableResourceSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_batch.types.consumable_resource_summary

ConsumableResourceSummaryList: TypeAlias = list[
    "aws_sdk_batch.types.consumable_resource_summary.ConsumableResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConsumableResourceSummaryList) -> list:
    import aws_sdk_batch.types.consumable_resource_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_batch.types.consumable_resource_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> ConsumableResourceSummaryList:
    import aws_sdk_batch.types.consumable_resource_summary

    out: ConsumableResourceSummaryList = []
    for item in data:
        out.append(
            aws_sdk_batch.types.consumable_resource_summary.deserialize_json(item)
        )
    return out
