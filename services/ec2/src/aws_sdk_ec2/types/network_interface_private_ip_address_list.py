"""Generated from Smithy shape ``com.amazonaws.ec2#NetworkInterfacePrivateIpAddressList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.network_interface_private_ip_address

NetworkInterfacePrivateIpAddressList: TypeAlias = list[
    "aws_sdk_ec2.types.network_interface_private_ip_address.NetworkInterfacePrivateIpAddress"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NetworkInterfacePrivateIpAddressList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.network_interface_private_ip_address

        aws_sdk_ec2.types.network_interface_private_ip_address.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> NetworkInterfacePrivateIpAddressList:
    import aws_sdk_ec2.types.network_interface_private_ip_address

    out: NetworkInterfacePrivateIpAddressList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.network_interface_private_ip_address.deserialize_ec2_query(
                child
            )
        )
    return out
