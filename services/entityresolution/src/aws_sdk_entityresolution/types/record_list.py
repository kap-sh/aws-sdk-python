"""Generated from Smithy shape ``com.amazonaws.entityresolution#RecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.record

RecordList: TypeAlias = list["aws_sdk_entityresolution.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: RecordList) -> list:
    import aws_sdk_entityresolution.types.record

    out: list = []
    for item in value:
        out.append(aws_sdk_entityresolution.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecordList:
    import aws_sdk_entityresolution.types.record

    out: RecordList = []
    for item in data:
        out.append(aws_sdk_entityresolution.types.record.deserialize_json(item))
    return out
