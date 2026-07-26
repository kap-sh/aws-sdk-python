"""Generated from Smithy shape ``com.amazonaws.lightsail#HostKeysList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.host_key_attributes

HostKeysList: TypeAlias = list[
    "capo_lightsail.types.host_key_attributes.HostKeyAttributes"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HostKeysList) -> list:
    import capo_lightsail.types.host_key_attributes

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.host_key_attributes.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> HostKeysList:
    import capo_lightsail.types.host_key_attributes

    out: HostKeysList = []
    for item in data:
        out.append(
            capo_lightsail.types.host_key_attributes.deserialize_aws_json_1_1(item)
        )
    return out
