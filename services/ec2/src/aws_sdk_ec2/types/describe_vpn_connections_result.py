"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeVpnConnectionsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.vpn_connection_list


class DescribeVpnConnectionsResult(TypedDict, closed=True):
    vpn_connections: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_list.VpnConnectionList"
    ]
    """<p>Information about one or more VPN connections.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DescribeVpnConnectionsResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_connections" in value:
        import aws_sdk_ec2.types.vpn_connection_list

        aws_sdk_ec2.types.vpn_connection_list.serialize_ec2_query(
            value["vpn_connections"], pairs, f"{prefix}.VpnConnectionSet"
        )


def deserialize_ec2_query(el: Element) -> DescribeVpnConnectionsResult:
    out: DescribeVpnConnectionsResult = {}  # type: ignore[typeddict-item]
    if el.find("VpnConnectionSet") is not None:
        import aws_sdk_ec2.types.vpn_connection_list

        out["vpn_connections"] = (
            aws_sdk_ec2.types.vpn_connection_list.deserialize_ec2_query(
                el, "VpnConnectionSet"
            )
        )
    return out
