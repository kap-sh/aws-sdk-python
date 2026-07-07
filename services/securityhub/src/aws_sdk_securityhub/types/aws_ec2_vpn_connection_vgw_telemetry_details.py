"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEc2VpnConnectionVgwTelemetryDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsEc2VpnConnectionVgwTelemetryDetails(TypedDict, closed=True):
    accepted_route_count: NotRequired["aws_sdk_securityhub.types.integer.Integer"]
    """<p>The number of accepted routes.</p>"""
    certificate_arn: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the VPN tunnel endpoint certificate.</p>"""
    last_status_change: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    r"""<p>The date and time of the last change in status.</p> <p>For more information about the validation and formatting of timestamp fields in Security Hub CSPM, see <a href=\"https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps\">Timestamps</a>.</p>"""
    outside_ip_address: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The Internet-routable IP address of the virtual private gateway's outside interface.</p>"""
    status: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The status of the VPN tunnel. Valid values are <code>DOWN</code> or <code>UP</code>.</p>"""
    status_message: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>If an error occurs, a description of the error.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEc2VpnConnectionVgwTelemetryDetails) -> dict:
    out: dict = {}
    if "accepted_route_count" in value:
        out["AcceptedRouteCount"] = value["accepted_route_count"]
    if "certificate_arn" in value:
        out["CertificateArn"] = value["certificate_arn"]
    if "last_status_change" in value:
        out["LastStatusChange"] = value["last_status_change"]
    if "outside_ip_address" in value:
        out["OutsideIpAddress"] = value["outside_ip_address"]
    if "status" in value:
        out["Status"] = value["status"]
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_json(data: dict) -> AwsEc2VpnConnectionVgwTelemetryDetails:
    out: AwsEc2VpnConnectionVgwTelemetryDetails = {}  # type: ignore[typeddict-item]
    if "AcceptedRouteCount" in data:
        out["accepted_route_count"] = data["AcceptedRouteCount"]
    if "CertificateArn" in data:
        out["certificate_arn"] = data["CertificateArn"]
    if "LastStatusChange" in data:
        out["last_status_change"] = data["LastStatusChange"]
    if "OutsideIpAddress" in data:
        out["outside_ip_address"] = data["OutsideIpAddress"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "StatusMessage" in data:
        out["status_message"] = data["StatusMessage"]
    return out
