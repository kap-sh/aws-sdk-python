"""Generated from Smithy shape ``com.amazonaws.backup#stringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.string

stringList: TypeAlias = list["aws_sdk_backup.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: stringList) -> list:
    return list(value)


def deserialize_json(data: list) -> stringList:
    return list(data)
