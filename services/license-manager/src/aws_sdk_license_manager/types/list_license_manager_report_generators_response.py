"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseManagerReportGeneratorsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.report_generator_list
    import aws_sdk_license_manager.types.string


class ListLicenseManagerReportGeneratorsResponse(TypedDict):
    report_generators: NotRequired[
        "aws_sdk_license_manager.types.report_generator_list.ReportGeneratorList"
    ]
    """<p>A report generator that creates periodic reports about your license configurations.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseManagerReportGeneratorsResponse) -> dict:
    out: dict = {}
    if "report_generators" in value:
        import aws_sdk_license_manager.types.report_generator_list

        out["ReportGenerators"] = (
            aws_sdk_license_manager.types.report_generator_list.serialize_aws_json_1_1(
                value["report_generators"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseManagerReportGeneratorsResponse:
    out: ListLicenseManagerReportGeneratorsResponse = {}  # type: ignore[typeddict-item]
    if "ReportGenerators" in data:
        import aws_sdk_license_manager.types.report_generator_list

        out["report_generators"] = (
            aws_sdk_license_manager.types.report_generator_list.deserialize_aws_json_1_1(
                data["ReportGenerators"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
