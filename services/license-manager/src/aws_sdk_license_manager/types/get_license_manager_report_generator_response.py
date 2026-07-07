"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseManagerReportGeneratorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.report_generator


class GetLicenseManagerReportGeneratorResponse(TypedDict, closed=True):
    report_generator: NotRequired[
        "aws_sdk_license_manager.types.report_generator.ReportGenerator"
    ]
    """<p>A report generator that creates periodic reports about your license configurations.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseManagerReportGeneratorResponse) -> dict:
    out: dict = {}
    if "report_generator" in value:
        import aws_sdk_license_manager.types.report_generator

        out["ReportGenerator"] = (
            aws_sdk_license_manager.types.report_generator.serialize_aws_json_1_1(
                value["report_generator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseManagerReportGeneratorResponse:
    out: GetLicenseManagerReportGeneratorResponse = {}  # type: ignore[typeddict-item]
    if "ReportGenerator" in data:
        import aws_sdk_license_manager.types.report_generator

        out["report_generator"] = (
            aws_sdk_license_manager.types.report_generator.deserialize_aws_json_1_1(
                data["ReportGenerator"]
            )
        )
    return out
