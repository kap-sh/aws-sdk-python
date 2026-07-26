"""Generated from Smithy shape ``com.amazonaws.route53#DeleteVPCAssociationAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.resource_id
    import capo_route_53.types.vpc


class DeleteVPCAssociationAuthorizationRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>When removing authorization to associate a VPC that was created by one Amazon Web Services account with a hosted zone that was created with a different Amazon Web Services account, the ID of the hosted zone.</p>"""
    vpc: "capo_route_53.types.vpc.VPC"
    """<p>When removing authorization to associate a VPC that was created by one Amazon Web Services account with a hosted zone that was created with a different Amazon Web Services account, a complex type that includes the ID and region of the VPC.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DeleteVPCAssociationAuthorizationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.vpc

    capo_route_53.types.vpc.serialize_xml(value["vpc"], el, "VPC")


def deserialize_xml(el: Element) -> DeleteVPCAssociationAuthorizationRequest:
    out: DeleteVPCAssociationAuthorizationRequest = {}  # type: ignore[typeddict-item]
    child_vpc = el.find("VPC")
    if child_vpc is not None:
        import capo_route_53.types.vpc

        out["vpc"] = capo_route_53.types.vpc.deserialize_xml(child_vpc)
    else:
        raise DeserializationError(
            "DeleteVPCAssociationAuthorizationRequest.vpc required"
        )
    return out
