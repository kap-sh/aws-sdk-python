"""Generated from Smithy shape ``com.amazonaws.clouddirectory#DirectoryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_clouddirectory.types.directory

DirectoryList: TypeAlias = list["capo_clouddirectory.types.directory.Directory"]


# --- restJson1 ser/de ---
def serialize_json(value: DirectoryList) -> list:
    import capo_clouddirectory.types.directory

    out: list = []
    for item in value:
        out.append(capo_clouddirectory.types.directory.serialize_json(item))
    return out


def deserialize_json(data: list) -> DirectoryList:
    import capo_clouddirectory.types.directory

    out: DirectoryList = []
    for item in data:
        out.append(capo_clouddirectory.types.directory.deserialize_json(item))
    return out
