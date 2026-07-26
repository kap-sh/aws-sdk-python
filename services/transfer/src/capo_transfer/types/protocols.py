"""Generated from Smithy shape ``com.amazonaws.transfer#Protocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.protocol

Protocols: TypeAlias = list["capo_transfer.types.protocol.Protocol"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Protocols) -> list:
    import capo_transfer.types.protocol

    out: list = []
    for item in value:
        out.append(capo_transfer.types.protocol.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Protocols:
    import capo_transfer.types.protocol

    out: Protocols = []
    for item in data:
        out.append(capo_transfer.types.protocol.deserialize_aws_json_1_1(item))
    return out
