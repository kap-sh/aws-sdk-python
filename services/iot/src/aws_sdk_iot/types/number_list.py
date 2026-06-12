"""Generated from Smithy shape ``com.amazonaws.iot#NumberList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.number

NumberList: TypeAlias = list["aws_sdk_iot.types.number.Number"]


# --- restJson1 ser/de ---
def serialize_json(value: NumberList) -> list:
    return list(value)


def deserialize_json(data: list) -> NumberList:
    return list(data)
