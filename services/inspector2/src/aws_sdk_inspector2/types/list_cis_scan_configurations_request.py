"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScanConfigurationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_scan_configurations_sort_by
    import aws_sdk_inspector2.types.cis_sort_order
    import aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria
    import aws_sdk_inspector2.types.list_cis_scan_configurations_max_results
    import aws_sdk_inspector2.types.next_token


class ListCisScanConfigurationsRequest(TypedDict, closed=True):
    filter_criteria: NotRequired[
        "aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria.ListCisScanConfigurationsFilterCriteria"
    ]
    """<p>The CIS scan configuration filter criteria.</p>"""
    sort_by: "aws_sdk_inspector2.types.cis_scan_configurations_sort_by.CisScanConfigurationsSortBy"
    """<p>The CIS scan configuration sort by order.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"]
    """<p>The CIS scan configuration sort order order.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""
    max_results: "aws_sdk_inspector2.types.list_cis_scan_configurations_max_results.ListCisScanConfigurationsMaxResults"
    """<p>The maximum number of CIS scan configurations to be returned in a single page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScanConfigurationsRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    import aws_sdk_inspector2.types.cis_scan_configurations_sort_by

    out["sortBy"] = (
        aws_sdk_inspector2.types.cis_scan_configurations_sort_by.serialize_json(
            value.get("sort_by", "SCAN_NAME")
        )
    )
    if "sort_order" in value:
        import aws_sdk_inspector2.types.cis_sort_order

        out["sortOrder"] = aws_sdk_inspector2.types.cis_sort_order.serialize_json(
            value["sort_order"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    out["maxResults"] = value.get("max_results", 100)
    return out


def deserialize_json(data: dict) -> ListCisScanConfigurationsRequest:
    out: ListCisScanConfigurationsRequest = {}  # type: ignore[typeddict-item]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.list_cis_scan_configurations_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "sortBy" in data:
        import aws_sdk_inspector2.types.cis_scan_configurations_sort_by

        out["sort_by"] = (
            aws_sdk_inspector2.types.cis_scan_configurations_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    else:
        out["sort_by"] = "SCAN_NAME"
    if "sortOrder" in data:
        import aws_sdk_inspector2.types.cis_sort_order

        out["sort_order"] = aws_sdk_inspector2.types.cis_sort_order.deserialize_json(
            data["sortOrder"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 100
    return out
