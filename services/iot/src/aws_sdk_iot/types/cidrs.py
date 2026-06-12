"""Generated from Smithy shape ``com.amazonaws.iot#Cidrs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.cidr

Cidrs: TypeAlias = list["aws_sdk_iot.types.cidr.Cidr"]


# --- restJson1 ser/de ---
def serialize_json(value: Cidrs) -> list:
    return list(value)


def deserialize_json(data: list) -> Cidrs:
    return list(data)
