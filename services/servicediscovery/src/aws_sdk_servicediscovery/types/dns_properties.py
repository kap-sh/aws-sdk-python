"""Generated from Smithy shape ``com.amazonaws.servicediscovery#DnsProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_servicediscovery.types.resource_id
    import aws_sdk_servicediscovery.types.soa


class DnsProperties(TypedDict, closed=True):
    hosted_zone_id: NotRequired["aws_sdk_servicediscovery.types.resource_id.ResourceId"]
    """<p>The ID for the Route 53 hosted zone that Cloud Map creates when you create a namespace.</p>"""
    soa: NotRequired["aws_sdk_servicediscovery.types.soa.SOA"]
    """<p>Start of Authority (SOA) record for the hosted zone.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsProperties) -> dict:
    out: dict = {}
    if "hosted_zone_id" in value:
        out["HostedZoneId"] = value["hosted_zone_id"]
    if "soa" in value:
        import aws_sdk_servicediscovery.types.soa

        out["SOA"] = aws_sdk_servicediscovery.types.soa.serialize_aws_json_1_1(
            value["soa"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DnsProperties:
    out: DnsProperties = {}  # type: ignore[typeddict-item]
    if "HostedZoneId" in data:
        out["hosted_zone_id"] = data["HostedZoneId"]
    if "SOA" in data:
        import aws_sdk_servicediscovery.types.soa

        out["soa"] = aws_sdk_servicediscovery.types.soa.deserialize_aws_json_1_1(
            data["SOA"]
        )
    return out
