"""Generated from Smithy shape ``com.amazonaws.ec2#VpnConnectionList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection

VpnConnectionList: TypeAlias = list["aws_sdk_ec2.types.vpn_connection.VpnConnection"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VpnConnectionList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.vpn_connection

        aws_sdk_ec2.types.vpn_connection.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> VpnConnectionList:
    import aws_sdk_ec2.types.vpn_connection

    out: VpnConnectionList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.vpn_connection.deserialize_ec2_query(child))
    return out
