"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseConversionTasksRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_integer
    import aws_sdk_license_manager.types.filters
    import aws_sdk_license_manager.types.string


class ListLicenseConversionTasksRequest(TypedDict):
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    filters: NotRequired["aws_sdk_license_manager.types.filters.Filters"]
    """<p> Filters to scope the results. Valid filters are <code>ResourceArns</code> and <code>Status</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseConversionTasksRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_license_manager.types.filters

        out["Filters"] = aws_sdk_license_manager.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseConversionTasksRequest:
    out: ListLicenseConversionTasksRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "Filters" in data:
        import aws_sdk_license_manager.types.filters

        out["filters"] = aws_sdk_license_manager.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    return out
