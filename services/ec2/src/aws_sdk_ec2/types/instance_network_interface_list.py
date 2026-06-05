"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceNetworkInterfaceList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_network_interface

InstanceNetworkInterfaceList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_network_interface.InstanceNetworkInterface"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceNetworkInterfaceList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_network_interface

        aws_sdk_ec2.types.instance_network_interface.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceNetworkInterfaceList:
    import aws_sdk_ec2.types.instance_network_interface

    out: InstanceNetworkInterfaceList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.instance_network_interface.deserialize_ec2_query(child)
        )
    return out
