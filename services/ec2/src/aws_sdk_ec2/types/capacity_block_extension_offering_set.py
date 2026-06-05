"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockExtensionOfferingSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_extension_offering

CapacityBlockExtensionOfferingSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_block_extension_offering.CapacityBlockExtensionOffering"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockExtensionOfferingSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_block_extension_offering

        aws_sdk_ec2.types.capacity_block_extension_offering.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> CapacityBlockExtensionOfferingSet:
    import aws_sdk_ec2.types.capacity_block_extension_offering

    out: CapacityBlockExtensionOfferingSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.capacity_block_extension_offering.deserialize_ec2_query(
                child
            )
        )
    return out
