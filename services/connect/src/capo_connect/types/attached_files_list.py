"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFilesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.attached_file

AttachedFilesList: TypeAlias = list["capo_connect.types.attached_file.AttachedFile"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFilesList) -> list:
    import capo_connect.types.attached_file

    out: list = []
    for item in value:
        out.append(capo_connect.types.attached_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachedFilesList:
    import capo_connect.types.attached_file

    out: AttachedFilesList = []
    for item in data:
        out.append(capo_connect.types.attached_file.deserialize_json(item))
    return out
