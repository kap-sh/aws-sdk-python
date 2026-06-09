"""Generated from Smithy shape ``com.amazonaws.ec2#AvailabilityZoneMessageList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.availability_zone_message

AvailabilityZoneMessageList: TypeAlias = list[
    "aws_sdk_ec2.types.availability_zone_message.AvailabilityZoneMessage"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AvailabilityZoneMessageList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.availability_zone_message

        aws_sdk_ec2.types.availability_zone_message.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AvailabilityZoneMessageList:
    import aws_sdk_ec2.types.availability_zone_message

    out: AvailabilityZoneMessageList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.availability_zone_message.deserialize_ec2_query(child)
        )
    return out
