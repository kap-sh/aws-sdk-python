"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateTransitGatewayMulticastDomainResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_associations


class AssociateTransitGatewayMulticastDomainResult(TypedDict):
    associations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_associations.TransitGatewayMulticastDomainAssociations"
    ]
    """<p>Information about the transit gateway multicast domain associations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociateTransitGatewayMulticastDomainResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "associations" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain_associations

        aws_sdk_ec2.types.transit_gateway_multicast_domain_associations.serialize_ec2_query(
            value["associations"], pairs, f"{prefix}.Associations"
        )


def deserialize_ec2_query(el: Element) -> AssociateTransitGatewayMulticastDomainResult:
    out: AssociateTransitGatewayMulticastDomainResult = {}  # type: ignore[typeddict-item]
    child_associations = el.find("Associations")
    if child_associations is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain_associations

        out["associations"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_domain_associations.deserialize_ec2_query(
                child_associations
            )
        )
    return out
