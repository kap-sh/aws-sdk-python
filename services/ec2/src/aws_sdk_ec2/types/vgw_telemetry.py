"""Generated from Smithy shape ``com.amazonaws.ec2#VgwTelemetry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.date_time
    import aws_sdk_ec2.types.integer
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.telemetry_status


class VgwTelemetry(TypedDict, closed=True):
    accepted_route_count: NotRequired["aws_sdk_ec2.types.integer.Integer"]
    """<p>The number of accepted routes.</p>"""
    last_status_change: NotRequired["aws_sdk_ec2.types.date_time.DateTime"]
    """<p>The date and time of the last change in status. This field is updated when changes in IKE (Phase 1), IPSec (Phase 2), or BGP status are detected.</p>"""
    outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Internet-routable IP address of the virtual private gateway's outside interface.</p>"""
    status: NotRequired["aws_sdk_ec2.types.telemetry_status.TelemetryStatus"]
    """<p>The status of the VPN tunnel.</p>"""
    status_message: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>If an error occurs, a description of the error.</p>"""
    certificate_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the VPN tunnel endpoint certificate.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VgwTelemetry, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "accepted_route_count" in value:
        pairs.append(
            (f"{prefix}.AcceptedRouteCount", str(value["accepted_route_count"]))
        )
    if "last_status_change" in value:
        import aws_sdk_ec2.types.date_time

        aws_sdk_ec2.types.date_time.serialize_ec2_query(
            value["last_status_change"], pairs, f"{prefix}.LastStatusChange"
        )
    if "outside_ip_address" in value:
        pairs.append((f"{prefix}.OutsideIpAddress", str(value["outside_ip_address"])))
    if "status" in value:
        import aws_sdk_ec2.types.telemetry_status

        aws_sdk_ec2.types.telemetry_status.serialize_ec2_query(
            value["status"], pairs, f"{prefix}.Status"
        )
    if "status_message" in value:
        pairs.append((f"{prefix}.StatusMessage", str(value["status_message"])))
    if "certificate_arn" in value:
        pairs.append((f"{prefix}.CertificateArn", str(value["certificate_arn"])))


def deserialize_ec2_query(el: Element) -> VgwTelemetry:
    out: VgwTelemetry = {}  # type: ignore[typeddict-item]
    child_accepted_route_count = el.find("AcceptedRouteCount")
    if child_accepted_route_count is not None:
        out["accepted_route_count"] = int(child_accepted_route_count.text or "")
    child_last_status_change = el.find("LastStatusChange")
    if child_last_status_change is not None:
        import aws_sdk_ec2.types.date_time

        out["last_status_change"] = aws_sdk_ec2.types.date_time.deserialize_ec2_query(
            child_last_status_change
        )
    child_outside_ip_address = el.find("OutsideIpAddress")
    if child_outside_ip_address is not None:
        out["outside_ip_address"] = str(child_outside_ip_address.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_ec2.types.telemetry_status

        out["status"] = aws_sdk_ec2.types.telemetry_status.deserialize_ec2_query(
            child_status
        )
    child_status_message = el.find("StatusMessage")
    if child_status_message is not None:
        out["status_message"] = str(child_status_message.text or "")
    child_certificate_arn = el.find("CertificateArn")
    if child_certificate_arn is not None:
        out["certificate_arn"] = str(child_certificate_arn.text or "")
    return out
