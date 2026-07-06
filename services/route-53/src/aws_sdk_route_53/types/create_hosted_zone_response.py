"""Generated from Smithy shape ``com.amazonaws.route53#CreateHostedZoneResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.change_info
    import aws_sdk_route_53.types.delegation_set
    import aws_sdk_route_53.types.hosted_zone
    import aws_sdk_route_53.types.resource_uri
    import aws_sdk_route_53.types.vpc


class CreateHostedZoneResponse(TypedDict, closed=True):
    hosted_zone: "aws_sdk_route_53.types.hosted_zone.HostedZone"
    """<p>A complex type that contains general information about the hosted zone.</p>"""
    change_info: "aws_sdk_route_53.types.change_info.ChangeInfo"
    """<p>A complex type that contains information about the <code>CreateHostedZone</code> request.</p>"""
    delegation_set: "aws_sdk_route_53.types.delegation_set.DelegationSet"
    """<p>A complex type that describes the name servers for this hosted zone.</p>"""
    vpc: NotRequired["aws_sdk_route_53.types.vpc.VPC"]
    """<p>A complex type that contains information about an Amazon VPC that you associated with this hosted zone.</p>"""
    location: "aws_sdk_route_53.types.resource_uri.ResourceURI"
    """<p>The unique URL representing the new hosted zone.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: CreateHostedZoneResponse, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    import aws_sdk_route_53.types.hosted_zone

    aws_sdk_route_53.types.hosted_zone.serialize_xml(
        value["hosted_zone"], el, "HostedZone"
    )
    import aws_sdk_route_53.types.change_info

    aws_sdk_route_53.types.change_info.serialize_xml(
        value["change_info"], el, "ChangeInfo"
    )
    import aws_sdk_route_53.types.delegation_set

    aws_sdk_route_53.types.delegation_set.serialize_xml(
        value["delegation_set"], el, "DelegationSet"
    )
    if "vpc" in value:
        import aws_sdk_route_53.types.vpc

        aws_sdk_route_53.types.vpc.serialize_xml(value["vpc"], el, "VPC")


def deserialize_xml(el: Element) -> CreateHostedZoneResponse:
    out: CreateHostedZoneResponse = {}  # type: ignore[typeddict-item]
    child_hosted_zone = el.find("HostedZone")
    if child_hosted_zone is not None:
        import aws_sdk_route_53.types.hosted_zone

        out["hosted_zone"] = aws_sdk_route_53.types.hosted_zone.deserialize_xml(
            child_hosted_zone
        )
    else:
        raise DeserializationError("CreateHostedZoneResponse.hosted_zone required")
    child_change_info = el.find("ChangeInfo")
    if child_change_info is not None:
        import aws_sdk_route_53.types.change_info

        out["change_info"] = aws_sdk_route_53.types.change_info.deserialize_xml(
            child_change_info
        )
    else:
        raise DeserializationError("CreateHostedZoneResponse.change_info required")
    child_delegation_set = el.find("DelegationSet")
    if child_delegation_set is not None:
        import aws_sdk_route_53.types.delegation_set

        out["delegation_set"] = aws_sdk_route_53.types.delegation_set.deserialize_xml(
            child_delegation_set
        )
    else:
        raise DeserializationError("CreateHostedZoneResponse.delegation_set required")
    child_vpc = el.find("VPC")
    if child_vpc is not None:
        import aws_sdk_route_53.types.vpc

        out["vpc"] = aws_sdk_route_53.types.vpc.deserialize_xml(child_vpc)
    return out
