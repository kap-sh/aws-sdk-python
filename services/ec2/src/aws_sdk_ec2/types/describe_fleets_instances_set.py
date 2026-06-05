"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeFleetsInstancesSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_fleets_instances

DescribeFleetsInstancesSet: TypeAlias = list[
    "aws_sdk_ec2.types.describe_fleets_instances.DescribeFleetsInstances"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeFleetsInstancesSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.describe_fleets_instances

        aws_sdk_ec2.types.describe_fleets_instances.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> DescribeFleetsInstancesSet:
    import aws_sdk_ec2.types.describe_fleets_instances

    out: DescribeFleetsInstancesSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.describe_fleets_instances.deserialize_ec2_query(child)
        )
    return out
