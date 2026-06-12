"""Generated from Smithy shape ``com.amazonaws.route53resolver#TargetAddress``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_route53resolver.types.ip
    import aws_sdk_route53resolver.types.ipv6
    import aws_sdk_route53resolver.types.port
    import aws_sdk_route53resolver.types.protocol
    import aws_sdk_route53resolver.types.server_name_indication


class TargetAddress(TypedDict):
    ip: NotRequired["aws_sdk_route53resolver.types.ip.Ip"]
    """<p>One IPv4 address that you want to forward DNS queries to.</p>"""
    port: NotRequired["aws_sdk_route53resolver.types.port.Port"]
    """<p>The port at <code>Ip</code> that you want to forward DNS queries to.</p>"""
    ipv6: NotRequired["aws_sdk_route53resolver.types.ipv6.Ipv6"]
    """<p> One IPv6 address that you want to forward DNS queries to. </p>"""
    protocol: NotRequired["aws_sdk_route53resolver.types.protocol.Protocol"]
    """<p> The protocols for the target address. The protocol you choose needs to be supported by the outbound endpoint of the Resolver rule.</p>"""
    server_name_indication: NotRequired[
        "aws_sdk_route53resolver.types.server_name_indication.ServerNameIndication"
    ]
    """<p> The Server Name Indication of the DoH server that you want to forward queries to. This is only used if the Protocol of the <code>TargetAddress</code> is <code>DoH</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetAddress) -> dict:
    out: dict = {}
    if "ip" in value:
        out["Ip"] = value["ip"]
    if "port" in value:
        out["Port"] = value["port"]
    if "ipv6" in value:
        out["Ipv6"] = value["ipv6"]
    if "protocol" in value:
        import aws_sdk_route53resolver.types.protocol

        out["Protocol"] = aws_sdk_route53resolver.types.protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "server_name_indication" in value:
        out["ServerNameIndication"] = value["server_name_indication"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetAddress:
    out: TargetAddress = {}  # type: ignore[typeddict-item]
    if "Ip" in data:
        out["ip"] = data["Ip"]
    if "Port" in data:
        out["port"] = data["Port"]
    if "Ipv6" in data:
        out["ipv6"] = data["Ipv6"]
    if "Protocol" in data:
        import aws_sdk_route53resolver.types.protocol

        out["protocol"] = (
            aws_sdk_route53resolver.types.protocol.deserialize_aws_json_1_1(
                data["Protocol"]
            )
        )
    if "ServerNameIndication" in data:
        out["server_name_indication"] = data["ServerNameIndication"]
    return out
