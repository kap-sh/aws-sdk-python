"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceTypeOfferingsList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_type_offering

InstanceTypeOfferingsList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_type_offering.InstanceTypeOffering"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceTypeOfferingsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_type_offering

        aws_sdk_ec2.types.instance_type_offering.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> InstanceTypeOfferingsList:
    import aws_sdk_ec2.types.instance_type_offering

    out: InstanceTypeOfferingsList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.instance_type_offering.deserialize_ec2_query(child)
        )
    return out
