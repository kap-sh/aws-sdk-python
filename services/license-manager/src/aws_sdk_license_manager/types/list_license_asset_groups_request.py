"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListLicenseAssetGroupsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.box_integer
    import aws_sdk_license_manager.types.filters
    import aws_sdk_license_manager.types.string


class ListLicenseAssetGroupsRequest(TypedDict, closed=True):
    filters: NotRequired["aws_sdk_license_manager.types.filters.Filters"]
    """<p>Filters to scope the results. Following filters are supported</p> <ul> <li> <p> <code>LicenseAssetRulesetArn</code> </p> </li> </ul>"""
    max_results: NotRequired["aws_sdk_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListLicenseAssetGroupsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_license_manager.types.filters

        out["Filters"] = aws_sdk_license_manager.types.filters.serialize_aws_json_1_1(
            value["filters"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListLicenseAssetGroupsRequest:
    out: ListLicenseAssetGroupsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_license_manager.types.filters

        out["filters"] = aws_sdk_license_manager.types.filters.deserialize_aws_json_1_1(
            data["Filters"]
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
