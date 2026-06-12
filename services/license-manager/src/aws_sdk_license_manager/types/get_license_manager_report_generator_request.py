"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseManagerReportGeneratorRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class GetLicenseManagerReportGeneratorRequest(TypedDict):
    license_manager_report_generator_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the report generator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseManagerReportGeneratorRequest) -> dict:
    out: dict = {}
    out["LicenseManagerReportGeneratorArn"] = value[
        "license_manager_report_generator_arn"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseManagerReportGeneratorRequest:
    out: GetLicenseManagerReportGeneratorRequest = {}  # type: ignore[typeddict-item]
    if "LicenseManagerReportGeneratorArn" in data:
        out["license_manager_report_generator_arn"] = data[
            "LicenseManagerReportGeneratorArn"
        ]
    else:
        raise DeserializationError(
            "GetLicenseManagerReportGeneratorRequest.license_manager_report_generator_arn required"
        )
    return out
