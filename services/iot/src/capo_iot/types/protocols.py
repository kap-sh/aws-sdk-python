"""Generated from Smithy shape ``com.amazonaws.iot#Protocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.protocol

Protocols: TypeAlias = list["capo_iot.types.protocol.Protocol"]


# --- restJson1 ser/de ---
def serialize_json(value: Protocols) -> list:
    import capo_iot.types.protocol

    out: list = []
    for item in value:
        out.append(capo_iot.types.protocol.serialize_json(item))
    return out


def deserialize_json(data: list) -> Protocols:
    import capo_iot.types.protocol

    out: Protocols = []
    for item in data:
        out.append(capo_iot.types.protocol.deserialize_json(item))
    return out
