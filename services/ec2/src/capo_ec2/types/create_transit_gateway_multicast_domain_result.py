"""Generated from Smithy shape ``com.amazonaws.ec2#CreateTransitGatewayMulticastDomainResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_domain


class CreateTransitGatewayMulticastDomainResult(TypedDict, closed=True):
    transit_gateway_multicast_domain: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_domain.TransitGatewayMulticastDomain"
    ]
    """<p>Information about the transit gateway multicast domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateTransitGatewayMulticastDomainResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "transit_gateway_multicast_domain" in value:
        import capo_ec2.types.transit_gateway_multicast_domain

        capo_ec2.types.transit_gateway_multicast_domain.serialize_ec2_query(
            value["transit_gateway_multicast_domain"],
            pairs,
            f"{key_prefix}TransitGatewayMulticastDomain",
        )


def deserialize_ec2_query(el: Element) -> CreateTransitGatewayMulticastDomainResult:
    out: CreateTransitGatewayMulticastDomainResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain = el.find("transitGatewayMulticastDomain")
    if child_transit_gateway_multicast_domain is not None:
        import capo_ec2.types.transit_gateway_multicast_domain

        out["transit_gateway_multicast_domain"] = (
            capo_ec2.types.transit_gateway_multicast_domain.deserialize_ec2_query(
                child_transit_gateway_multicast_domain
            )
        )
    return out
