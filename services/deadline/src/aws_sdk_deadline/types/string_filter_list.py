"""Generated from Smithy shape ``com.amazonaws.deadline#StringFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_deadline.types.string_filter

StringFilterList: TypeAlias = list["aws_sdk_deadline.types.string_filter.StringFilter"]


# --- restJson1 ser/de ---
def serialize_json(value: StringFilterList) -> list:
    return list(value)


def deserialize_json(data: list) -> StringFilterList:
    return list(data)
