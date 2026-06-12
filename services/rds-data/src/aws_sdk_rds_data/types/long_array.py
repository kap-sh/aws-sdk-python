"""Generated from Smithy shape ``com.amazonaws.rdsdata#LongArray``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.boxed_long

LongArray: TypeAlias = list["aws_sdk_rds_data.types.boxed_long.BoxedLong | None"]


# --- restJson1 ser/de ---
def serialize_json(value: LongArray) -> list:
    return list(value)


def deserialize_json(data: list) -> LongArray:
    return list(data)
