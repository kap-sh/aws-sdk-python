"""Generated from Smithy shape ``com.amazonaws.cognitosync#RecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cognito_sync.types.record

RecordList: TypeAlias = list["capo_cognito_sync.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: RecordList) -> list:
    import capo_cognito_sync.types.record

    out: list = []
    for item in value:
        out.append(capo_cognito_sync.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecordList:
    import capo_cognito_sync.types.record

    out: RecordList = []
    for item in data:
        out.append(capo_cognito_sync.types.record.deserialize_json(item))
    return out
