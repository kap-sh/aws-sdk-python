"""Generated from Smithy shape ``com.amazonaws.appintegrations#FolderList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.non_blank_long_string

FolderList: TypeAlias = list["aws_sdk_appintegrations.types.non_blank_long_string.NonBlankLongString"]


# --- restJson1 ser/de ---
def serialize_json(value: FolderList) -> list:
    return list(value)


def deserialize_json(data: list) -> FolderList:
    return list(data)