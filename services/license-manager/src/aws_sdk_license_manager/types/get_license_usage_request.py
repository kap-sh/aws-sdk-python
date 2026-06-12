"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.arn


class GetLicenseUsageRequest(TypedDict):
    license_arn: "aws_sdk_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseUsageRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseUsageRequest:
    out: GetLicenseUsageRequest = {}  # type: ignore[typeddict-item]
    if "LicenseArn" in data:
        out["license_arn"] = data["LicenseArn"]
    else:
        raise DeserializationError("GetLicenseUsageRequest.license_arn required")
    return out
