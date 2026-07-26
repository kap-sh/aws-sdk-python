"""Generated from Smithy shape ``com.amazonaws.entityresolution#RecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.record

RecordList: TypeAlias = list["capo_entityresolution.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: RecordList) -> list:
    import capo_entityresolution.types.record

    out: list = []
    for item in value:
        out.append(capo_entityresolution.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecordList:
    import capo_entityresolution.types.record

    out: RecordList = []
    for item in data:
        out.append(capo_entityresolution.types.record.deserialize_json(item))
    return out
