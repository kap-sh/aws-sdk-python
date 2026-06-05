"""Generated from Smithy shape ``com.amazonaws.ec2#GetTransitGatewayMulticastDomainAssociationsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list


class GetTransitGatewayMulticastDomainAssociationsResult(TypedDict):
    multicast_domain_associations: NotRequired[
        "aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list.TransitGatewayMulticastDomainAssociationList"
    ]
    """<p>Information about the multicast domain associations.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The token to use to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: GetTransitGatewayMulticastDomainAssociationsResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "multicast_domain_associations" in value:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list

        aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list.serialize_ec2_query(
            value["multicast_domain_associations"],
            pairs,
            f"{prefix}.MulticastDomainAssociations",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))


def deserialize_ec2_query(
    el: Element,
) -> GetTransitGatewayMulticastDomainAssociationsResult:
    out: GetTransitGatewayMulticastDomainAssociationsResult = {}  # type: ignore[typeddict-item]
    if el.find("MulticastDomainAssociations") is not None:
        import aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list

        out["multicast_domain_associations"] = (
            aws_sdk_ec2.types.transit_gateway_multicast_domain_association_list.deserialize_ec2_query(
                el, "MulticastDomainAssociations"
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out
