"""Generated from Smithy shape ``com.amazonaws.ec2#MovingAddressStatusSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.moving_address_status

MovingAddressStatusSet: TypeAlias = list[
    "aws_sdk_ec2.types.moving_address_status.MovingAddressStatus"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: MovingAddressStatusSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.moving_address_status

        aws_sdk_ec2.types.moving_address_status.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> MovingAddressStatusSet:
    import aws_sdk_ec2.types.moving_address_status

    out: MovingAddressStatusSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.moving_address_status.deserialize_ec2_query(child))
    return out
