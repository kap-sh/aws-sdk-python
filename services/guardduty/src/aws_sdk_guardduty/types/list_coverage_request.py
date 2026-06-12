"""Generated from Smithy shape ``com.amazonaws.guardduty#ListCoverageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.coverage_filter_criteria
    import aws_sdk_guardduty.types.coverage_sort_criteria
    import aws_sdk_guardduty.types.detector_id
    import aws_sdk_guardduty.types.max_results
    import aws_sdk_guardduty.types.string


class ListCoverageRequest(TypedDict):
    detector_id: "aws_sdk_guardduty.types.detector_id.DetectorId"
    """<p>The unique ID of the detector whose coverage details you want to retrieve.</p> <p>To find the <code>detectorId</code> in the current Region, see the Settings page in the GuardDuty console, or run the <a href=\"https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html\">ListDetectors</a> API.</p>"""
    next_token: NotRequired["aws_sdk_guardduty.types.string.String"]
    """<p>A token to use for paginating results that are returned in the response. Set the value of this parameter to null for the first request to a list action. For subsequent calls, use the NextToken value returned from the previous request to continue listing results after the first page.</p>"""
    max_results: NotRequired["aws_sdk_guardduty.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""
    filter_criteria: NotRequired[
        "aws_sdk_guardduty.types.coverage_filter_criteria.CoverageFilterCriteria"
    ]
    """<p>Represents the criteria used to filter the coverage details.</p>"""
    sort_criteria: NotRequired[
        "aws_sdk_guardduty.types.coverage_sort_criteria.CoverageSortCriteria"
    ]
    """<p>Represents the criteria used to sort the coverage details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCoverageRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filter_criteria" in value:
        import aws_sdk_guardduty.types.coverage_filter_criteria

        out["filterCriteria"] = (
            aws_sdk_guardduty.types.coverage_filter_criteria.serialize_json(
                value["filter_criteria"]
            )
        )
    if "sort_criteria" in value:
        import aws_sdk_guardduty.types.coverage_sort_criteria

        out["sortCriteria"] = (
            aws_sdk_guardduty.types.coverage_sort_criteria.serialize_json(
                value["sort_criteria"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListCoverageRequest:
    out: ListCoverageRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filterCriteria" in data:
        import aws_sdk_guardduty.types.coverage_filter_criteria

        out["filter_criteria"] = (
            aws_sdk_guardduty.types.coverage_filter_criteria.deserialize_json(
                data["filterCriteria"]
            )
        )
    if "sortCriteria" in data:
        import aws_sdk_guardduty.types.coverage_sort_criteria

        out["sort_criteria"] = (
            aws_sdk_guardduty.types.coverage_sort_criteria.deserialize_json(
                data["sortCriteria"]
            )
        )
    return out
