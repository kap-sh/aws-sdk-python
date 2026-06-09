"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfacePrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address

InstanceSecondaryInterfacePrivateIpAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.instance_secondary_interface_private_ip_address.InstanceSecondaryInterfacePrivateIpAddress"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSecondaryInterfacePrivateIpAddressList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address

        aws_sdk_ec2.types.instance_secondary_interface_private_ip_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> InstanceSecondaryInterfacePrivateIpAddressList:
    import aws_sdk_ec2.types.instance_secondary_interface_private_ip_address

    out: InstanceSecondaryInterfacePrivateIpAddressList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.instance_secondary_interface_private_ip_address.deserialize_ec2_query(
                child
            )
        )
    return out
