"""Generated from Smithy shape ``com.amazonaws.entityresolution#UniqueIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.header_safe_unique_id

UniqueIdList: TypeAlias = list[
    "aws_sdk_entityresolution.types.header_safe_unique_id.HeaderSafeUniqueId"
]


# --- restJson1 ser/de ---
def serialize_json(value: UniqueIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> UniqueIdList:
    return list(data)
