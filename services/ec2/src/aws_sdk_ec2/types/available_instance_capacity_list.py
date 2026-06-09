"""Generated from Smithy shape ``com.amazonaws.ec2#AvailableInstanceCapacityList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_capacity

AvailableInstanceCapacityList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_capacity.InstanceCapacity"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailableInstanceCapacityList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_capacity

        aws_sdk_ec2.types.instance_capacity.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AvailableInstanceCapacityList:
    import aws_sdk_ec2.types.instance_capacity

    out: AvailableInstanceCapacityList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.instance_capacity.deserialize_ec2_query(child))
    return out
