"""Generated from Smithy shape ``com.amazonaws.ram#SourceArnOrAccountList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ram.types.string

SourceArnOrAccountList: TypeAlias = list["aws_sdk_ram.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: SourceArnOrAccountList) -> list:
    return list(value)


def deserialize_json(data: list) -> SourceArnOrAccountList:
    return list(data)
