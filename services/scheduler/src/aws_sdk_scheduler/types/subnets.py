"""Generated from Smithy shape ``com.amazonaws.scheduler#Subnets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.subnet

Subnets: TypeAlias = list["aws_sdk_scheduler.types.subnet.Subnet"]


# --- restJson1 ser/de ---
def serialize_json(value: Subnets) -> list:
    return list(value)


def deserialize_json(data: list) -> Subnets:
    return list(data)
