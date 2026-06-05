"""Generated from Smithy shape ``com.amazonaws.ec2#CapacityManagerConditionSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.capacity_manager_condition

CapacityManagerConditionSet: TypeAlias = list[
    "aws_sdk_ec2.types.capacity_manager_condition.CapacityManagerCondition"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CapacityManagerConditionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.capacity_manager_condition

        aws_sdk_ec2.types.capacity_manager_condition.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CapacityManagerConditionSet:
    import aws_sdk_ec2.types.capacity_manager_condition

    out: CapacityManagerConditionSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.capacity_manager_condition.deserialize_ec2_query(child)
        )
    return out
