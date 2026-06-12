"""Generated from Smithy shape ``com.amazonaws.licensemanager#CreateLicenseManagerReportGeneratorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class CreateLicenseManagerReportGeneratorResponse(TypedDict):
    license_manager_report_generator_arn: NotRequired[
        "aws_sdk_license_manager.types.string.String"
    ]
    """<p>The Amazon Resource Name (ARN) of the new report generator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLicenseManagerReportGeneratorResponse) -> dict:
    out: dict = {}
    if "license_manager_report_generator_arn" in value:
        out["LicenseManagerReportGeneratorArn"] = value[
            "license_manager_report_generator_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLicenseManagerReportGeneratorResponse:
    out: CreateLicenseManagerReportGeneratorResponse = {}  # type: ignore[typeddict-item]
    if "LicenseManagerReportGeneratorArn" in data:
        out["license_manager_report_generator_arn"] = data[
            "LicenseManagerReportGeneratorArn"
        ]
    return out
