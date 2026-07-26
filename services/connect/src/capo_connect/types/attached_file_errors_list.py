"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFileErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.attached_file_error

AttachedFileErrorsList: TypeAlias = list[
    "capo_connect.types.attached_file_error.AttachedFileError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFileErrorsList) -> list:
    import capo_connect.types.attached_file_error

    out: list = []
    for item in value:
        out.append(capo_connect.types.attached_file_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachedFileErrorsList:
    import capo_connect.types.attached_file_error

    out: AttachedFileErrorsList = []
    for item in data:
        out.append(capo_connect.types.attached_file_error.deserialize_json(item))
    return out
