"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityBlockStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_block_status

CapacityBlockStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_block_status.CapacityBlockStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityBlockStatusSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_block_status

        aws_sdk_ec2.types.capacity_block_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CapacityBlockStatusSet:
    import aws_sdk_ec2.types.capacity_block_status

    out: CapacityBlockStatusSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.capacity_block_status.deserialize_ec2_query(child))
    return out
