"""Generated from Smithy shape ``com.amazonaws.route53#HostedZoneSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_route_53._protocol.xml import Element, SubElement
from aws_sdk_route_53.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_route_53.types.dns_name
    import aws_sdk_route_53.types.hosted_zone_owner
    import aws_sdk_route_53.types.resource_id


class HostedZoneSummary(TypedDict):
    hosted_zone_id: "aws_sdk_route_53.types.resource_id.ResourceId"
    """<p>The Route 53 hosted zone ID of a private hosted zone that the specified VPC is associated with.</p>"""
    name: "aws_sdk_route_53.types.dns_name.DNSName"
    """<p>The name of the private hosted zone, such as <code>example.com</code>.</p>"""
    owner: "aws_sdk_route_53.types.hosted_zone_owner.HostedZoneOwner"
    """<p>The owner of a private hosted zone that the specified VPC is associated with. The owner can be either an Amazon Web Services account or an Amazon Web Services service.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HostedZoneSummary, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    SubElement(el, "HostedZoneId").text = str(value["hosted_zone_id"])
    SubElement(el, "Name").text = str(value["name"])
    import aws_sdk_route_53.types.hosted_zone_owner

    aws_sdk_route_53.types.hosted_zone_owner.serialize_xml(value["owner"], el, "Owner")


def deserialize_xml(el: Element) -> HostedZoneSummary:
    out: HostedZoneSummary = {}  # type: ignore[typeddict-item]
    child_hosted_zone_id = el.find("HostedZoneId")
    if child_hosted_zone_id is not None:
        out["hosted_zone_id"] = str(child_hosted_zone_id.text or "")
    else:
        raise DeserializationError("HostedZoneSummary.hosted_zone_id required")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    else:
        raise DeserializationError("HostedZoneSummary.name required")
    child_owner = el.find("Owner")
    if child_owner is not None:
        import aws_sdk_route_53.types.hosted_zone_owner

        out["owner"] = aws_sdk_route_53.types.hosted_zone_owner.deserialize_xml(
            child_owner
        )
    else:
        raise DeserializationError("HostedZoneSummary.owner required")
    return out
