"""Generated from Smithy shape ``com.amazonaws.datazone#FilterIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.filter_id

FilterIds: TypeAlias = list["aws_sdk_datazone.types.filter_id.FilterId"]


# --- restJson1 ser/de ---
def serialize_json(value: FilterIds) -> list:
    return list(value)


def deserialize_json(data: list) -> FilterIds:
    return list(data)
