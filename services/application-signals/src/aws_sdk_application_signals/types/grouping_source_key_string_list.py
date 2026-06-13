"""Generated from Smithy shape ``com.amazonaws.applicationsignals#GroupingSourceKeyStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.grouping_string

GroupingSourceKeyStringList: TypeAlias = list[
    "aws_sdk_application_signals.types.grouping_string.GroupingString"
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupingSourceKeyStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> GroupingSourceKeyStringList:
    return list(data)
