"""Generated from Smithy shape ``com.amazonaws.route53#HealthCheckObservation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_route_53._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import aws_sdk_route_53.types.health_check_region
    import aws_sdk_route_53.types.ip_address
    import aws_sdk_route_53.types.status_report


class HealthCheckObservation(TypedDict):
    region: NotRequired["aws_sdk_route_53.types.health_check_region.HealthCheckRegion"]
    """<p>The region of the Amazon Route 53 health checker that provided the status in <code>StatusReport</code>.</p>"""
    ip_address: NotRequired["aws_sdk_route_53.types.ip_address.IPAddress"]
    """<p>The IP address of the Amazon Route 53 health checker that provided the failure reason in <code>StatusReport</code>.</p>"""
    status_report: NotRequired["aws_sdk_route_53.types.status_report.StatusReport"]
    """<p>A complex type that contains the last failure reason as reported by one Amazon Route 53 health checker and the time of the failed health check.</p>"""


# --- restXml ser/de ---
def serialize_xml(value: HealthCheckObservation, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "region" in value:
        import aws_sdk_route_53.types.health_check_region

        aws_sdk_route_53.types.health_check_region.serialize_xml(
            value["region"], el, "Region"
        )
    if "ip_address" in value:
        SubElement(el, "IPAddress").text = str(value["ip_address"])
    if "status_report" in value:
        import aws_sdk_route_53.types.status_report

        aws_sdk_route_53.types.status_report.serialize_xml(
            value["status_report"], el, "StatusReport"
        )


def deserialize_xml(el: Element) -> HealthCheckObservation:
    out: HealthCheckObservation = {}  # type: ignore[typeddict-item]
    child_region = el.find("Region")
    if child_region is not None:
        import aws_sdk_route_53.types.health_check_region

        out["region"] = aws_sdk_route_53.types.health_check_region.deserialize_xml(
            child_region
        )
    child_ip_address = el.find("IPAddress")
    if child_ip_address is not None:
        out["ip_address"] = str(child_ip_address.text or "")
    child_status_report = el.find("StatusReport")
    if child_status_report is not None:
        import aws_sdk_route_53.types.status_report

        out["status_report"] = aws_sdk_route_53.types.status_report.deserialize_xml(
            child_status_report
        )
    return out
