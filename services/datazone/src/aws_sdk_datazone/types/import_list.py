"""Generated from Smithy shape ``com.amazonaws.datazone#ImportList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_datazone.types.import_

ImportList: TypeAlias = list["aws_sdk_datazone.types.import_.Import"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportList) -> list:
    import aws_sdk_datazone.types.import_

    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.import_.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportList:
    import aws_sdk_datazone.types.import_

    out: ImportList = []
    for item in data:
        out.append(aws_sdk_datazone.types.import_.deserialize_json(item))
    return out
