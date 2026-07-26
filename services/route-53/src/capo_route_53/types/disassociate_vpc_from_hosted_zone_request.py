"""Generated from Smithy shape ``com.amazonaws.route53#DisassociateVPCFromHostedZoneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.disassociate_vpc_comment
    import capo_route_53.types.resource_id
    import capo_route_53.types.vpc


class DisassociateVPCFromHostedZoneRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the private hosted zone that you want to disassociate a VPC from.</p>"""
    vpc: "capo_route_53.types.vpc.VPC"
    """<p>A complex type that contains information about the VPC that you're disassociating from the specified hosted zone.</p>"""
    comment: NotRequired[
        "capo_route_53.types.disassociate_vpc_comment.DisassociateVPCComment"
    ]
    """<p> <i>Optional:</i> A comment about the disassociation request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: DisassociateVPCFromHostedZoneRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.vpc

    capo_route_53.types.vpc.serialize_xml(value["vpc"], el, "VPC")
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> DisassociateVPCFromHostedZoneRequest:
    out: DisassociateVPCFromHostedZoneRequest = {}  # type: ignore[typeddict-item]
    child_vpc = el.find("VPC")
    if child_vpc is not None:
        import capo_route_53.types.vpc

        out["vpc"] = capo_route_53.types.vpc.deserialize_xml(child_vpc)
    else:
        raise DeserializationError("DisassociateVPCFromHostedZoneRequest.vpc required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
