"""Generated from Smithy shape ``com.amazonaws.inspector2#ListCisScansRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cis_sort_order
    import aws_sdk_inspector2.types.list_cis_scans_detail_level
    import aws_sdk_inspector2.types.list_cis_scans_filter_criteria
    import aws_sdk_inspector2.types.list_cis_scans_max_results
    import aws_sdk_inspector2.types.list_cis_scans_sort_by
    import aws_sdk_inspector2.types.next_token


class ListCisScansRequest(TypedDict):
    filter_criteria: NotRequired[
        "aws_sdk_inspector2.types.list_cis_scans_filter_criteria.ListCisScansFilterCriteria"
    ]
    """<p>The CIS scan filter criteria.</p>"""
    detail_level: NotRequired[
        "aws_sdk_inspector2.types.list_cis_scans_detail_level.ListCisScansDetailLevel"
    ]
    """<p>The detail applied to the CIS scan.</p>"""
    sort_by: "aws_sdk_inspector2.types.list_cis_scans_sort_by.ListCisScansSortBy"
    """<p>The CIS scans sort by order.</p>"""
    sort_order: NotRequired["aws_sdk_inspector2.types.cis_sort_order.CisSortOrder"]
    """<p>The CIS scans sort order.</p>"""
    next_token: NotRequired["aws_sdk_inspector2.types.next_token.NextToken"]
    """<p>The pagination token from a previous request that's used to retrieve the next page of results.</p>"""
    max_results: (
        "aws_sdk_inspector2.types.list_cis_scans_max_results.ListCisScansMaxResults"
    )
    """<p>The maximum number of results to be returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCisScansRequest) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import aws_sdk_inspector2.types.list_cis_scans_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_inspector2.types.list_cis_scans_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "detail_level" in value:
        import aws_sdk_inspector2.types.list_cis_scans_detail_level

        out["detailLevel"] = (
            aws_sdk_inspector2.types.list_cis_scans_detail_level.serialize_json(
                value["detail_level"]
            )
        )
    import aws_sdk_inspector2.types.list_cis_scans_sort_by

    out["sortBy"] = aws_sdk_inspector2.types.list_cis_scans_sort_by.serialize_json(
        value.get("sort_by", "SCAN_START_DATE")
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


def deserialize_json(data: dict) -> ListCisScansRequest:
    out: ListCisScansRequest = {}  # type: ignore[typeddict-item]
    if "filterCriteria" in data:
        import aws_sdk_inspector2.types.list_cis_scans_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_inspector2.types.list_cis_scans_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "detailLevel" in data:
        import aws_sdk_inspector2.types.list_cis_scans_detail_level

        out["detail_level"] = (
            aws_sdk_inspector2.types.list_cis_scans_detail_level.deserialize_json(
                data["detailLevel"]
            )
        )
    if "sortBy" in data:
        import aws_sdk_inspector2.types.list_cis_scans_sort_by

        out["sort_by"] = (
            aws_sdk_inspector2.types.list_cis_scans_sort_by.deserialize_json(
                data["sortBy"]
            )
        )
    else:
        out["sort_by"] = "SCAN_START_DATE"
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
