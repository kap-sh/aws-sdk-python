"""Generated from Smithy shape ``com.amazonaws.lightsail#InstancePortStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.instance_port_state

InstancePortStateList: TypeAlias = list[
    "capo_lightsail.types.instance_port_state.InstancePortState"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstancePortStateList) -> list:
    import capo_lightsail.types.instance_port_state

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.instance_port_state.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> InstancePortStateList:
    import capo_lightsail.types.instance_port_state

    out: InstancePortStateList = []
    for item in data:
        out.append(
            capo_lightsail.types.instance_port_state.deserialize_aws_json_1_1(item)
        )
    return out
