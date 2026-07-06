"""Generated from Smithy shape ``com.amazonaws.route53#CreateVPCAssociationAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.resource_id
    import aws_sdk_route_53.types.vpc


class CreateVPCAssociationAuthorizationRequest(TypedDict, closed=True):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The ID of the private hosted zone that you want to authorize associating a VPC with.</p>"""
    vpc: "aws_sdk_route_53.types.vpc.VPC"
    """<p>A complex type that contains the VPC ID and region for the VPC that you want to authorize associating with your hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(
    value: CreateVPCAssociationAuthorizationRequest, parent: Element, tag: str
) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.vpc

    aws_sdk_route_53.types.vpc.serialize_xml(value["vpc"], el, "VPC")


def deserialize_xml(el: Element) -> CreateVPCAssociationAuthorizationRequest:
    out: CreateVPCAssociationAuthorizationRequest = {}  # type: ignore[typeddict-item]
    child_vpc = el.find("VPC")
    if child_vpc is not None:
        import aws_sdk_route_53.types.vpc

        out["vpc"] = aws_sdk_route_53.types.vpc.deserialize_xml(child_vpc)
    else:
        raise DeserializationError(
            "CreateVPCAssociationAuthorizationRequest.vpc required"
        )
    return out
