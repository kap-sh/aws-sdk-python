"""Generated from Smithy shape ``com.amazonaws.transfer#As2Transports``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transfer.types.as2_transport

As2Transports: TypeAlias = list["aws_sdk_transfer.types.as2_transport.As2Transport"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: As2Transports) -> list:
    import aws_sdk_transfer.types.as2_transport

    out: list = []
    for item in value:
        out.append(aws_sdk_transfer.types.as2_transport.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> As2Transports:
    import aws_sdk_transfer.types.as2_transport

    out: As2Transports = []
    for item in data:
        out.append(aws_sdk_transfer.types.as2_transport.deserialize_aws_json_1_1(item))
    return out
