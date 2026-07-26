"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.resource_statistics

GroupedByResource: TypeAlias = list[
    "capo_guardduty.types.resource_statistics.ResourceStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByResource) -> list:
    import capo_guardduty.types.resource_statistics

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.resource_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByResource:
    import capo_guardduty.types.resource_statistics

    out: GroupedByResource = []
    for item in data:
        out.append(capo_guardduty.types.resource_statistics.deserialize_json(item))
    return out
