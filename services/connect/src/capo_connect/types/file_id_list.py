"""Generated from Smithy shape ``com.amazonaws.connect#FileIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.file_id

FileIdList: TypeAlias = list["capo_connect.types.file_id.FileId"]


# --- restJson1 ser/de ---
def serialize_json(value: FileIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> FileIdList:
    return list(data)
