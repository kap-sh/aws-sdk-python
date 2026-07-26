"""Generated from Smithy shape ``com.amazonaws.backup#FormatList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.string

FormatList: TypeAlias = list["capo_backup.types.string.string"]


# --- restJson1 ser/de ---
def serialize_json(value: FormatList) -> list:
    return list(value)


def deserialize_json(data: list) -> FormatList:
    return list(data)
