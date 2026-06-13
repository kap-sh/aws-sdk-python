"""Generated from Smithy shape ``com.amazonaws.wisdom#GroupingValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.grouping_value

GroupingValues: TypeAlias = list["aws_sdk_wisdom.types.grouping_value.GroupingValue"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingValues) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupingValues:
    return list(data)
