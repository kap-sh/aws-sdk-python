"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_topology

InstanceSet: TypeAlias = list["aws_sdk_ec2.types.instance_topology.InstanceTopology"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_topology

        aws_sdk_ec2.types.instance_topology.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceSet:
    import aws_sdk_ec2.types.instance_topology

    out: InstanceSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance_topology.deserialize_ec2_query(child))
    return out
