"""Generated from Smithy shape ``com.amazonaws.route53#AssociateVPCWithHostedZoneRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_route_53._protocol.xml import Element, SubElement
from capo_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import capo_route_53.types.associate_vpc_comment
    import capo_route_53.types.resource_id
    import capo_route_53.types.vpc


class AssociateVPCWithHostedZoneRequest(TypedDict, closed=True):
    hosted_zone_id: "capo_route_53.types.resource_id.ResourceId"
    """<p>The ID of the private hosted zone that you want to associate an Amazon VPC with.</p> <p>Note that you can't associate a VPC with a hosted zone that doesn't have an existing VPC association.</p>"""
    vpc: "capo_route_53.types.vpc.VPC"
    """<p>A complex type that contains information about the VPC that you want to associate with a private hosted zone.</p>"""
    comment: NotRequired[
        "capo_route_53.types.associate_vpc_comment.AssociateVPCComment"
    ]
    """<p> <i>Optional:</i> A comment about the association request.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: AssociateVPCWithHostedZoneRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import capo_route_53.types.vpc

    capo_route_53.types.vpc.serialize_xml(value["vpc"], el, "VPC")
    if "comment" in value:
        SubElement(el, "Comment").text = str(value["comment"])


def deserialize_xml(el: Element) -> AssociateVPCWithHostedZoneRequest:
    out: AssociateVPCWithHostedZoneRequest = {}  # type: ignore[typeddict-item]
    child_vpc = el.find("VPC")
    if child_vpc is not None:
        import capo_route_53.types.vpc

        out["vpc"] = capo_route_53.types.vpc.deserialize_xml(child_vpc)
    else:
        raise DeserializationError("AssociateVPCWithHostedZoneRequest.vpc required")
    child_comment = el.find("Comment")
    if child_comment is not None:
        out["comment"] = str(child_comment.text or "")
    return out
