"""Generated from Smithy shape ``com.amazonaws.cognitosync#RecordList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cognito_sync.types.record

RecordList: TypeAlias = list["aws_sdk_cognito_sync.types.record.Record"]


# --- restJson1 ser/de ---
def serialize_json(value: RecordList) -> list:
    import aws_sdk_cognito_sync.types.record

    out: list = []
    for item in value:
        out.append(aws_sdk_cognito_sync.types.record.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecordList:
    import aws_sdk_cognito_sync.types.record

    out: RecordList = []
    for item in data:
        out.append(aws_sdk_cognito_sync.types.record.deserialize_json(item))
    return out
