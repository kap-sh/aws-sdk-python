"""Generated from Smithy shape ``com.amazonaws.iot#Targets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.target

Targets: TypeAlias = list["aws_sdk_iot.types.target.Target"]


# --- restJson1 ser/de ---
def serialize_json(value: Targets) -> list:
    return list(value)


def deserialize_json(data: list) -> Targets:
    return list(data)
