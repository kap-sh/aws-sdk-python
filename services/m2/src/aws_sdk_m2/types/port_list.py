"""Generated from Smithy shape ``com.amazonaws.m2#PortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_m2.types.integer

PortList: TypeAlias = list["aws_sdk_m2.types.integer.Integer"]


# --- restJson1 ser/de ---
def serialize_json(value: PortList) -> list:
    return list(value)


def deserialize_json(data: list) -> PortList:
    return list(data)
