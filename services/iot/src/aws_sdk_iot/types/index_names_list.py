"""Generated from Smithy shape ``com.amazonaws.iot#IndexNamesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.index_name

IndexNamesList: TypeAlias = list["aws_sdk_iot.types.index_name.IndexName"]


# --- restJson1 ser/de ---
def serialize_json(value: IndexNamesList) -> list:
    return list(value)


def deserialize_json(data: list) -> IndexNamesList:
    return list(data)
