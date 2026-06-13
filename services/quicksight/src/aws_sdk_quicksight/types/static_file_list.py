"""Generated from Smithy shape ``com.amazonaws.quicksight#StaticFileList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.static_file

StaticFileList: TypeAlias = list["aws_sdk_quicksight.types.static_file.StaticFile"]


# --- restJson1 ser/de ---
def serialize_json(value: StaticFileList) -> list:
    import aws_sdk_quicksight.types.static_file

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.static_file.serialize_json(item))
    return out


def deserialize_json(data: list) -> StaticFileList:
    import aws_sdk_quicksight.types.static_file

    out: StaticFileList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.static_file.deserialize_json(item))
    return out
