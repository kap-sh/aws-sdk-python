"""Generated from Smithy shape ``com.amazonaws.rtbfabric#ProtocolList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rtbfabric.types.protocol

ProtocolList: TypeAlias = list["aws_sdk_rtbfabric.types.protocol.Protocol"]


# --- restJson1 ser/de ---
def serialize_json(value: ProtocolList) -> list:
    import aws_sdk_rtbfabric.types.protocol

    out: list = []
    for item in value:
        out.append(aws_sdk_rtbfabric.types.protocol.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProtocolList:
    import aws_sdk_rtbfabric.types.protocol

    out: ProtocolList = []
    for item in data:
        out.append(aws_sdk_rtbfabric.types.protocol.deserialize_json(item))
    return out
