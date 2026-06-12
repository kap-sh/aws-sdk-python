"""Generated from Smithy shape ``com.amazonaws.route53#GetHostedZoneResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.delegation_set
    import aws_sdk_route_53.types.hosted_zone
    import aws_sdk_route_53.types.vp_cs


class GetHostedZoneResponse(TypedDict):
    hosted_zone: "aws_sdk_route_53.types.hosted_zone.HostedZone"
    """<p>A complex type that contains general information about the specified hosted zone.</p>"""
    delegation_set: NotRequired["aws_sdk_route_53.types.delegation_set.DelegationSet"]
    """<p>A complex type that lists the Amazon Route 53 name servers for the specified hosted zone.</p>"""
    vp_cs: NotRequired["aws_sdk_route_53.types.vp_cs.VPCs"]
    """<p>A complex type that contains information about the VPCs that are associated with the specified hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: GetHostedZoneResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.hosted_zone

    aws_sdk_route_53.types.hosted_zone.serialize_xml(
        value["hosted_zone"], el, "HostedZone"
    )
    if "delegation_set" in value:
        import aws_sdk_route_53.types.delegation_set

        aws_sdk_route_53.types.delegation_set.serialize_xml(
            value["delegation_set"], el, "DelegationSet"
        )
    if "vp_cs" in value:
        import aws_sdk_route_53.types.vp_cs

        aws_sdk_route_53.types.vp_cs.serialize_xml(value["vp_cs"], el, "VPCs")


def deserialize_xml(el: Element) -> GetHostedZoneResponse:
    out: GetHostedZoneResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zone = el.find("HostedZone")
    if child_hosted_zone is not None:
        import aws_sdk_route_53.types.hosted_zone

        out["hosted_zone"] = aws_sdk_route_53.types.hosted_zone.deserialize_xml(
            child_hosted_zone
        )
    else:
        raise DeserializationError("GetHostedZoneResponse.hosted_zone required")
    child_delegation_set = el.find("DelegationSet")
    if child_delegation_set is not None:
        import aws_sdk_route_53.types.delegation_set

        out["delegation_set"] = aws_sdk_route_53.types.delegation_set.deserialize_xml(
            child_delegation_set
        )
    child_vp_cs = el.find("VPCs")
    if child_vp_cs is not None:
        import aws_sdk_route_53.types.vp_cs

        out["vp_cs"] = aws_sdk_route_53.types.vp_cs.deserialize_xml(child_vp_cs)
    return out
