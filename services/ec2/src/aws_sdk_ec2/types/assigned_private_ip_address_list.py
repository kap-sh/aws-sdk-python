"""Generated from Smithy shape ``com.amazonaws.ec2#AssignedPrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.assigned_private_ip_address

AssignedPrivateIpAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.assigned_private_ip_address.AssignedPrivateIpAddress"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssignedPrivateIpAddressList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.assigned_private_ip_address

        aws_sdk_ec2.types.assigned_private_ip_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AssignedPrivateIpAddressList:
    import aws_sdk_ec2.types.assigned_private_ip_address

    out: AssignedPrivateIpAddressList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.assigned_private_ip_address.deserialize_ec2_query(child)
        )
    return out
