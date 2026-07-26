"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SetIpAddressTypeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.ip_address_type
    import capo_elastic_load_balancing_v2.types.load_balancer_arn


class SetIpAddressTypeInput(TypedDict, closed=True):
    load_balancer_arn: NotRequired[
        "capo_elastic_load_balancing_v2.types.load_balancer_arn.LoadBalancerArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the load balancer.</p>"""
    ip_address_type: NotRequired[
        "capo_elastic_load_balancing_v2.types.ip_address_type.IpAddressType"
    ]
    """<p>The IP address type. Internal load balancers must use <code>ipv4</code>.</p> <p>[Application Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses), <code>dualstack</code> (IPv4 and IPv6 addresses), and <code>dualstack-without-public-ipv4</code> (public IPv6 addresses and private IPv4 and IPv6 addresses).</p> <p>Application Load Balancer authentication supports IPv4 addresses only when connecting to an Identity Provider (IdP) or Amazon Cognito endpoint. Without a public IPv4 address the load balancer can't complete the authentication process, resulting in HTTP 500 errors.</p> <p>[Network Load Balancers and Gateway Load Balancers] The possible values are <code>ipv4</code> (IPv4 addresses) and <code>dualstack</code> (IPv4 and IPv6 addresses).</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: SetIpAddressTypeInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "load_balancer_arn" in value:
        pairs.append((f"{prefix}.LoadBalancerArn", str(value["load_balancer_arn"])))
    if "ip_address_type" in value:
        import capo_elastic_load_balancing_v2.types.ip_address_type

        capo_elastic_load_balancing_v2.types.ip_address_type.serialize_query(
            value["ip_address_type"], pairs, f"{prefix}.IpAddressType"
        )


def deserialize_query(el: Element) -> SetIpAddressTypeInput:
    out: SetIpAddressTypeInput = {}  # type: ignore[typeddict-item]
    child_load_balancer_arn = el.find("LoadBalancerArn")
    if child_load_balancer_arn is not None:
        out["load_balancer_arn"] = str(child_load_balancer_arn.text or "")
    child_ip_address_type = el.find("IpAddressType")
    if child_ip_address_type is not None:
        import capo_elastic_load_balancing_v2.types.ip_address_type

        out["ip_address_type"] = (
            capo_elastic_load_balancing_v2.types.ip_address_type.deserialize_query(
                child_ip_address_type
            )
        )
    return out
