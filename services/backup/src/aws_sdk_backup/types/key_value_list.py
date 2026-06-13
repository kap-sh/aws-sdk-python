"""Generated from Smithy shape ``com.amazonaws.backup#KeyValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup.types.key_value

KeyValueList: TypeAlias = list["aws_sdk_backup.types.key_value.KeyValue"]


# --- restJson1 ser/de ---
def serialize_json(value: KeyValueList) -> list:
    import aws_sdk_backup.types.key_value

    out: list = []
    for item in value:
        out.append(aws_sdk_backup.types.key_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> KeyValueList:
    import aws_sdk_backup.types.key_value

    out: KeyValueList = []
    for item in data:
        out.append(aws_sdk_backup.types.key_value.deserialize_json(item))
    return out
