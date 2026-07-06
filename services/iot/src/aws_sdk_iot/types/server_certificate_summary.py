"""Generated from Smithy shape ``com.amazonaws.iot#ServerCertificateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.acm_certificate_arn
    import aws_sdk_iot.types.server_certificate_status
    import aws_sdk_iot.types.server_certificate_status_detail


class ServerCertificateSummary(TypedDict, closed=True):
    server_certificate_arn: NotRequired[
        "aws_sdk_iot.types.acm_certificate_arn.AcmCertificateArn"
    ]
    """<p>The ARN of the server certificate.</p>"""
    server_certificate_status: NotRequired[
        "aws_sdk_iot.types.server_certificate_status.ServerCertificateStatus"
    ]
    """<p>The status of the server certificate.</p>"""
    server_certificate_status_detail: NotRequired[
        "aws_sdk_iot.types.server_certificate_status_detail.ServerCertificateStatusDetail"
    ]
    """<p>Details that explain the status of the server certificate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerCertificateSummary) -> dict:
    out: dict = {}
    if "server_certificate_arn" in value:
        out["serverCertificateArn"] = value["server_certificate_arn"]
    if "server_certificate_status" in value:
        import aws_sdk_iot.types.server_certificate_status

        out["serverCertificateStatus"] = (
            aws_sdk_iot.types.server_certificate_status.serialize_json(
                value["server_certificate_status"]
            )
        )
    if "server_certificate_status_detail" in value:
        out["serverCertificateStatusDetail"] = value["server_certificate_status_detail"]
    return out


def deserialize_json(data: dict) -> ServerCertificateSummary:
    out: ServerCertificateSummary = {}  # type: ignore[typeddict-item]
    if "serverCertificateArn" in data:
        out["server_certificate_arn"] = data["serverCertificateArn"]
    if "serverCertificateStatus" in data:
        import aws_sdk_iot.types.server_certificate_status

        out["server_certificate_status"] = (
            aws_sdk_iot.types.server_certificate_status.deserialize_json(
                data["serverCertificateStatus"]
            )
        )
    if "serverCertificateStatusDetail" in data:
        out["server_certificate_status_detail"] = data["serverCertificateStatusDetail"]
    return out
