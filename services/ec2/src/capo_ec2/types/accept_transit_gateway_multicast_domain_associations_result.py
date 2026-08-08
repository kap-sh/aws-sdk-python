"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptTransitGatewayMulticastDomainAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.transit_gateway_multicast_domain_associations


class AcceptTransitGatewayMulticastDomainAssociationsResult(TypedDict, closed=True):
    associations: NotRequired[
        "capo_ec2.types.transit_gateway_multicast_domain_associations.TransitGatewayMulticastDomainAssociations"
    ]
    """<p>Information about the multicast domain associations.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceptTransitGatewayMulticastDomainAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "associations" in value:
        import capo_ec2.types.transit_gateway_multicast_domain_associations

        capo_ec2.types.transit_gateway_multicast_domain_associations.serialize_ec2_query(
            value["associations"], pairs, f"{key_prefix}Associations"
        )


def deserialize_ec2_query(
    el: Element,
) -> AcceptTransitGatewayMulticastDomainAssociationsResult:
    out: AcceptTransitGatewayMulticastDomainAssociationsResult = {}  # type: ignore[typeddict-item]
    child_associations = el.find("associations")
    if child_associations is not None:
        import capo_ec2.types.transit_gateway_multicast_domain_associations

        out["associations"] = (
            capo_ec2.types.transit_gateway_multicast_domain_associations.deserialize_ec2_query(
                child_associations
            )
        )
    return out
