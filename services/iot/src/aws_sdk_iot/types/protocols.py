"""Generated from Smithy shape ``com.amazonaws.iot#Protocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.protocol

Protocols: TypeAlias = list["aws_sdk_iot.types.protocol.Protocol"]


# --- restJson1 ser/de ---
def serialize_json(value: Protocols) -> list:
    import aws_sdk_iot.types.protocol

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.protocol.serialize_json(item))
    return out


def deserialize_json(data: list) -> Protocols:
    import aws_sdk_iot.types.protocol

    out: Protocols = []
    for item in data:
        out.append(aws_sdk_iot.types.protocol.deserialize_json(item))
    return out
