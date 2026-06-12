"""Generated from Smithy shape ``com.amazonaws.connect#AttachedFileErrorsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.attached_file_error

AttachedFileErrorsList: TypeAlias = list[
    "aws_sdk_connect.types.attached_file_error.AttachedFileError"
]


# --- restJson1 ser/de ---
def serialize_json(value: AttachedFileErrorsList) -> list:
    import aws_sdk_connect.types.attached_file_error

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.attached_file_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> AttachedFileErrorsList:
    import aws_sdk_connect.types.attached_file_error

    out: AttachedFileErrorsList = []
    for item in data:
        out.append(aws_sdk_connect.types.attached_file_error.deserialize_json(item))
    return out
