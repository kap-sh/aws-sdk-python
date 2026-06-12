"""Generated from Smithy shape ``com.amazonaws.rdsdata#BooleanArray``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.boxed_boolean

BooleanArray: TypeAlias = list[
    "aws_sdk_rds_data.types.boxed_boolean.BoxedBoolean | None"
]


# --- restJson1 ser/de ---
def serialize_json(value: BooleanArray) -> list:
    return list(value)


def deserialize_json(data: list) -> BooleanArray:
    return list(data)
