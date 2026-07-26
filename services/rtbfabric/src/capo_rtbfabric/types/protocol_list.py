"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ProtocolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_rtbfabric.types.protocol

ProtocolList: TypeAlias = list["capo_rtbfabric.types.protocol.Protocol"]


# --- restJson1 ser/de ---
def serialize_json(value: ProtocolList) -> list:
    import capo_rtbfabric.types.protocol

    out: list = []
    for item in value:
        out.append(capo_rtbfabric.types.protocol.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProtocolList:
    import capo_rtbfabric.types.protocol

    out: ProtocolList = []
    for item in data:
        out.append(capo_rtbfabric.types.protocol.deserialize_json(item))
    return out
