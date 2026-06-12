"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseManagerReportGeneratorsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.filter_list
    import aws_sdk_license_manager.types.max_size100
    import aws_sdk_license_manager.types.string


class ListLicenseManagerReportGeneratorsRequest(TypedDict):
    filters: NotRequired["aws_sdk_license_manager.types.filter_list.FilterList"]
    """<p>Filters to scope the results. The following filters are supported: </p> <ul> <li> <p> <code>LicenseConfigurationArn</code> </p> </li> </ul>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_license_manager.types.max_size100.MaxSize100"]
    """<p>Maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseManagerReportGeneratorsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_license_manager.types.filter_list

        out["Filters"] = (
            aws_sdk_license_manager.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseManagerReportGeneratorsRequest:
    out: ListLicenseManagerReportGeneratorsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_license_manager.types.filter_list

        out["filters"] = (
            aws_sdk_license_manager.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
