"""Generated from Smithy shape ``com.amazonaws.guardduty#GroupedByResource``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.resource_statistics

GroupedByResource: TypeAlias = list[
    "aws_sdk_guardduty.types.resource_statistics.ResourceStatistics"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupedByResource) -> list:
    import aws_sdk_guardduty.types.resource_statistics

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.resource_statistics.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupedByResource:
    import aws_sdk_guardduty.types.resource_statistics

    out: GroupedByResource = []
    for item in data:
        out.append(aws_sdk_guardduty.types.resource_statistics.deserialize_json(item))
    return out
