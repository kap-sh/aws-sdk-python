"""Generated from Smithy shape ``com.amazonaws.backup#KeyValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_backup.types.key_value

KeyValueList: TypeAlias = list["capo_backup.types.key_value.KeyValue"]


# --- restJson1 ser/de ---
def serialize_json(value: KeyValueList) -> list:
    import capo_backup.types.key_value

    out: list = []
    for item in value:
        out.append(capo_backup.types.key_value.serialize_json(item))
    return out


def deserialize_json(data: list) -> KeyValueList:
    import capo_backup.types.key_value

    out: KeyValueList = []
    for item in data:
        out.append(capo_backup.types.key_value.deserialize_json(item))
    return out
