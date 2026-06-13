"""Generated from Smithy shape ``com.amazonaws.mgn#ImportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.import_task

ImportList: TypeAlias = list["aws_sdk_mgn.types.import_task.ImportTask"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportList) -> list:
    import aws_sdk_mgn.types.import_task

    out: list = []
    for item in value:
        out.append(aws_sdk_mgn.types.import_task.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportList:
    import aws_sdk_mgn.types.import_task

    out: ImportList = []
    for item in data:
        out.append(aws_sdk_mgn.types.import_task.deserialize_json(item))
    return out
