"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceResourceSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.space_resource_summary

SpaceResourceSummaries: TypeAlias = list[
    "capo_quicksight.types.space_resource_summary.SpaceResourceSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceResourceSummaries) -> list:
    import capo_quicksight.types.space_resource_summary

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.space_resource_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> SpaceResourceSummaries:
    import capo_quicksight.types.space_resource_summary

    out: SpaceResourceSummaries = []
    for item in data:
        out.append(capo_quicksight.types.space_resource_summary.deserialize_json(item))
    return out
