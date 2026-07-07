"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseManagerReportGeneratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.string


class DeleteLicenseManagerReportGeneratorRequest(TypedDict, closed=True):
    license_manager_report_generator_arn: "aws_sdk_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the report generator to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseManagerReportGeneratorRequest) -> dict:
    out: dict = {}
    out["LicenseManagerReportGeneratorArn"] = value[
        "license_manager_report_generator_arn"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseManagerReportGeneratorRequest:
    out: DeleteLicenseManagerReportGeneratorRequest = {}  # type: ignore[typeddict-item]
    if "LicenseManagerReportGeneratorArn" in data:
        out["license_manager_report_generator_arn"] = data[
            "LicenseManagerReportGeneratorArn"
        ]
    else:
        raise DeserializationError(
            "DeleteLicenseManagerReportGeneratorRequest.license_manager_report_generator_arn required"
        )
    return out
