"""Generated from Smithy shape ``com.amazonaws.lightsail#HostKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.host_key_attributes

HostKeysList: TypeAlias = list[
    "aws_sdk_lightsail.types.host_key_attributes.HostKeyAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostKeysList) -> list:
    import aws_sdk_lightsail.types.host_key_attributes

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lightsail.types.host_key_attributes.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HostKeysList:
    import aws_sdk_lightsail.types.host_key_attributes

    out: HostKeysList = []
    for item in data:
        out.append(
            aws_sdk_lightsail.types.host_key_attributes.deserialize_aws_json_1_1(item)
        )
    return out
