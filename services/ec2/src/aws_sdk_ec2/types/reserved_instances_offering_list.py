"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesOfferingList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_offering

ReservedInstancesOfferingList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_offering.ReservedInstancesOffering"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesOfferingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.reserved_instances_offering

        aws_sdk_ec2.types.reserved_instances_offering.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ReservedInstancesOfferingList:
    import aws_sdk_ec2.types.reserved_instances_offering

    out: ReservedInstancesOfferingList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.reserved_instances_offering.deserialize_ec2_query(child)
        )
    return out
