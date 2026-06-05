"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteTransitGatewayMulticastDomainResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_domain


class DeleteTransitGatewayMulticastDomainResult(TypedDict):
    transit_gateway_multicast_domain: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain.TransitGatewayMulticastDomain"
    ]
    """<p>Information about the deleted transit gateway multicast domain.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DeleteTransitGatewayMulticastDomainResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "transit_gateway_multicast_domain" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain

        aws_sdk_ec2.types.transit_gateway_multicast_domain.serialize_ec2_query(
            value["transit_gateway_multicast_domain"],
            pairs,
            f"{prefix}.TransitGatewayMulticastDomain",
        )


def deserialize_ec2_query(el: Element) -> DeleteTransitGatewayMulticastDomainResult:
    out: DeleteTransitGatewayMulticastDomainResult = {}  # type: ignore[typeddict-item]
    child_transit_gateway_multicast_domain = el.find("TransitGatewayMulticastDomain")
    if child_transit_gateway_multicast_domain is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain

        out["transit_gateway_multicast_domain"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_domain.deserialize_ec2_query(
                child_transit_gateway_multicast_domain
            )
        )
    return out
