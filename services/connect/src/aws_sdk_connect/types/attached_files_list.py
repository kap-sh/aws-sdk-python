"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFilesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.attached_file

AttachedFilesList: TypeAlias = list["aws_sdk_connect.types.attached_file.AttachedFile"]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFilesList) -> list:
    import aws_sdk_connect.types.attached_file

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.attached_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachedFilesList:
    import aws_sdk_connect.types.attached_file

    out: AttachedFilesList = []
    for item in data:
        out.append(aws_sdk_connect.types.attached_file.deserialize_json(item))
    return out
