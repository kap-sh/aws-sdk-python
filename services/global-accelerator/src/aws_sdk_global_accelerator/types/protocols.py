"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Protocols``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.protocol

Protocols: TypeAlias = list["aws_sdk_global_accelerator.types.protocol.Protocol"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Protocols) -> list:
    import aws_sdk_global_accelerator.types.protocol

    out: list = []
    for item in value:
        out.append(
            aws_sdk_global_accelerator.types.protocol.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Protocols:
    import aws_sdk_global_accelerator.types.protocol

    out: Protocols = []
    for item in data:
        out.append(
            aws_sdk_global_accelerator.types.protocol.deserialize_aws_json_1_1(item)
        )
    return out
