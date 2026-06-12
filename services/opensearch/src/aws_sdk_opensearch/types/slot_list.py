"""Generated from Smithy shape ``com.amazonaws.opensearch#SlotList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.long

SlotList: TypeAlias = list["aws_sdk_opensearch.types.long.Long"]


# --- restJson1 ser/de ---
def serialize_json(value: SlotList) -> list:
    return list(value)


def deserialize_json(data: list) -> SlotList:
    return list(data)
