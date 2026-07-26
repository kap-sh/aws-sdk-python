"""Generated from Smithy shape ``com.amazonaws.lightsail#PortList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.port

PortList: TypeAlias = list["capo_lightsail.types.port.Port"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> PortList:
    return list(data)
