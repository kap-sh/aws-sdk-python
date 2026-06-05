"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnectionSet``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.client_vpn_connection

ClientVpnConnectionSet: TypeAlias = list[
    "aws_sdk_ec2.types.client_vpn_connection.ClientVpnConnection"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnConnectionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.client_vpn_connection

        aws_sdk_ec2.types.client_vpn_connection.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ClientVpnConnectionSet:
    import aws_sdk_ec2.types.client_vpn_connection

    out: ClientVpnConnectionSet = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.client_vpn_connection.deserialize_ec2_query(child))
    return out
