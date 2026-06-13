"""Generated from Smithy shape ``com.amazonaws.datazone#ImportList``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_datazone.types.import

ImportList: TypeAlias = list["aws_sdk_datazone.types.import.Import"]


# --- restJson1 ser/de ---
def serialize_json(value: ImportList) -> list:
    import aws_sdk_datazone.types.import
    out: list = []
    for item in value:
        out.append(aws_sdk_datazone.types.import.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImportList:
    import aws_sdk_datazone.types.import
    out: ImportList = []
    for item in data:
        out.append(aws_sdk_datazone.types.import.deserialize_json(item))
    return out