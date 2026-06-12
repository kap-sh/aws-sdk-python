"""Generated from Smithy shape ``com.amazonaws.connect#ResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.string

ResourceTypeList: TypeAlias = list["aws_sdk_connect.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceTypeList:
    return list(data)
