"""Generated from Smithy shape ``com.amazonaws.m2#String20List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.string20

String20List: TypeAlias = list["aws_sdk_m2.types.string20.String20"]


# --- restJson1 ser/de ---
def serialize_json(value: String20List) -> list:
    return list(value)


def deserialize_json(data: list) -> String20List:
    return list(data)
