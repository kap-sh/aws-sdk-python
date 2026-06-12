"""Generated from Smithy shape ``com.amazonaws.connect#OriginsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.origin

OriginsList: TypeAlias = list["aws_sdk_connect.types.origin.Origin"]


# --- restJson1 ser/de ---
def serialize_json(value: OriginsList) -> list:
    return list(value)


def deserialize_json(data: list) -> OriginsList:
    return list(data)
