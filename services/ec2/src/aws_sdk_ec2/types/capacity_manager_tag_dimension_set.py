"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerTagDimensionSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_tag_dimension

CapacityManagerTagDimensionSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_tag_dimension.CapacityManagerTagDimension"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerTagDimensionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_manager_tag_dimension

        aws_sdk_ec2.types.capacity_manager_tag_dimension.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CapacityManagerTagDimensionSet:
    import aws_sdk_ec2.types.capacity_manager_tag_dimension

    out: CapacityManagerTagDimensionSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.capacity_manager_tag_dimension.deserialize_ec2_query(
                child
            )
        )
    return out
