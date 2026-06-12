"""Generated from Smithy shape ``com.amazonaws.lightsail#AccessReceiverList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.resource_receiving_access

AccessReceiverList: TypeAlias = list[
    "aws_sdk_lightsail.types.resource_receiving_access.ResourceReceivingAccess"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccessReceiverList) -> list:
    import aws_sdk_lightsail.types.resource_receiving_access

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.resource_receiving_access.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> AccessReceiverList:
    import aws_sdk_lightsail.types.resource_receiving_access

    out: AccessReceiverList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.resource_receiving_access.deserialize_aws_json_1_1(
                item
            )
        )
    return out
