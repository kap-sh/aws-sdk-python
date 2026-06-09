"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockOfferingSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_offering

CapacityBlockOfferingSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_block_offering.CapacityBlockOffering"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockOfferingSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_block_offering

        aws_sdk_ec2.types.capacity_block_offering.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CapacityBlockOfferingSet:
    import aws_sdk_ec2.types.capacity_block_offering

    out: CapacityBlockOfferingSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.capacity_block_offering.deserialize_ec2_query(child)
        )
    return out
