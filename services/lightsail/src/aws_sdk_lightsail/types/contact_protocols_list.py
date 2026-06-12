"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactProtocolsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.contact_protocol

ContactProtocolsList: TypeAlias = list[
    "aws_sdk_lightsail.types.contact_protocol.ContactProtocol"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactProtocolsList) -> list:
    import aws_sdk_lightsail.types.contact_protocol

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.contact_protocol.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ContactProtocolsList:
    import aws_sdk_lightsail.types.contact_protocol

    out: ContactProtocolsList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.contact_protocol.deserialize_aws_json_1_1(item)
        )
    return out
