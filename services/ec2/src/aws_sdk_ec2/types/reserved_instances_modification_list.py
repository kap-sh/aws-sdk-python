"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModificationList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_modification

ReservedInstancesModificationList: TypeAlias = list[
    "aws_sdk_ec2.types.reserved_instances_modification.ReservedInstancesModification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesModificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.reserved_instances_modification

        aws_sdk_ec2.types.reserved_instances_modification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> ReservedInstancesModificationList:
    import aws_sdk_ec2.types.reserved_instances_modification

    out: ReservedInstancesModificationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.reserved_instances_modification.deserialize_ec2_query(
                child
            )
        )
    return out
