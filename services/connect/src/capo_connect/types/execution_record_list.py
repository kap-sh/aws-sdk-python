"""Generated from Smithy shape ``com.amazonaws.connect#ExecutionRecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.execution_record

ExecutionRecordList: TypeAlias = list[
    "capo_connect.types.execution_record.ExecutionRecord"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExecutionRecordList) -> list:
    import capo_connect.types.execution_record

    out: list = []
    for item in value:
        out.append(capo_connect.types.execution_record.serialize_json(item))
    return out


def deserialize_json(data: list) -> ExecutionRecordList:
    import capo_connect.types.execution_record

    out: ExecutionRecordList = []
    for item in data:
        out.append(capo_connect.types.execution_record.deserialize_json(item))
    return out
