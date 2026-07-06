"""Generated from Smithy shape ``com.amazonaws.deadline#LicenseEndpointSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.license_endpoint_id
    import aws_sdk_deadline.types.license_endpoint_status
    import aws_sdk_deadline.types.status_message
    import aws_sdk_deadline.types.vpc_id


class LicenseEndpointSummary(TypedDict, closed=True):
    license_endpoint_id: NotRequired[
        "aws_sdk_deadline.types.license_endpoint_id.LicenseEndpointId"
    ]
    """<p>The license endpoint ID.</p>"""
    status: NotRequired[
        "aws_sdk_deadline.types.license_endpoint_status.LicenseEndpointStatus"
    ]
    """<p>The status of the license endpoint.</p>"""
    status_message: NotRequired["aws_sdk_deadline.types.status_message.StatusMessage"]
    """<p>The status message of the license endpoint.</p>"""
    vpc_id: NotRequired["aws_sdk_deadline.types.vpc_id.VpcId"]
    """<p>The VPC (virtual private cloud) ID associated with the license endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseEndpointSummary) -> dict:
    out: dict = {}
    if "license_endpoint_id" in value:
        out["licenseEndpointId"] = value["license_endpoint_id"]
    if "status" in value:
        import aws_sdk_deadline.types.license_endpoint_status

        out["status"] = aws_sdk_deadline.types.license_endpoint_status.serialize_json(
            value["status"]
        )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    return out


def deserialize_json(data: dict) -> LicenseEndpointSummary:
    out: LicenseEndpointSummary = {}  # type: ignore[typeddict-item]
    if "licenseEndpointId" in data:
        out["license_endpoint_id"] = data["licenseEndpointId"]
    if "status" in data:
        import aws_sdk_deadline.types.license_endpoint_status

        out["status"] = aws_sdk_deadline.types.license_endpoint_status.deserialize_json(
            data["status"]
        )
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    return out
