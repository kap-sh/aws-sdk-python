"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceConnectEndpointPublicDnsNames``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_connect_endpoint_dns_names


class InstanceConnectEndpointPublicDnsNames(TypedDict, closed=True):
    ipv4: NotRequired[
        "capo_ec2.types.instance_connect_endpoint_dns_names.InstanceConnectEndpointDnsNames"
    ]
    """<p>The IPv4-only DNS name of the EC2 Instance Connect Endpoint.</p>"""
    dualstack: NotRequired[
        "capo_ec2.types.instance_connect_endpoint_dns_names.InstanceConnectEndpointDnsNames"
    ]
    """<p>The dualstack DNS name of the EC2 Instance Connect Endpoint. A dualstack DNS name supports connections from both IPv4 and IPv6 clients.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceConnectEndpointPublicDnsNames,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "ipv4" in value:
        import capo_ec2.types.instance_connect_endpoint_dns_names

        capo_ec2.types.instance_connect_endpoint_dns_names.serialize_ec2_query(
            value["ipv4"], pairs, f"{key_prefix}Ipv4"
        )
    if "dualstack" in value:
        import capo_ec2.types.instance_connect_endpoint_dns_names

        capo_ec2.types.instance_connect_endpoint_dns_names.serialize_ec2_query(
            value["dualstack"], pairs, f"{key_prefix}Dualstack"
        )


def deserialize_ec2_query(el: Element) -> InstanceConnectEndpointPublicDnsNames:
    out: InstanceConnectEndpointPublicDnsNames = {}  # type: ignore[typeddict-item]
    child_ipv4 = el.find("ipv4")
    if child_ipv4 is not None:
        import capo_ec2.types.instance_connect_endpoint_dns_names

        out["ipv4"] = (
            capo_ec2.types.instance_connect_endpoint_dns_names.deserialize_ec2_query(
                child_ipv4
            )
        )
    child_dualstack = el.find("dualstack")
    if child_dualstack is not None:
        import capo_ec2.types.instance_connect_endpoint_dns_names

        out["dualstack"] = (
            capo_ec2.types.instance_connect_endpoint_dns_names.deserialize_ec2_query(
                child_dualstack
            )
        )
    return out
