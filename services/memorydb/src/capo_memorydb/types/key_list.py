"""Generated from Smithy shape ``com.amazonaws.memorydb#KeyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_memorydb.types.string

KeyList: TypeAlias = list["capo_memorydb.types.string.String"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> KeyList:
    return list(data)
