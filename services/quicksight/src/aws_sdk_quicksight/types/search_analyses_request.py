"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchAnalysesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.analysis_search_filter_list
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.string


class SearchAnalysesRequest(TypedDict):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the analyses that you're searching for.</p>"""
    filters: (
        "aws_sdk_quicksight.types.analysis_search_filter_list.AnalysisSearchFilterList"
    )
    """<p>The structure for the search filters that you want to apply to your search. </p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchAnalysesRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.analysis_search_filter_list

    out["Filters"] = (
        aws_sdk_quicksight.types.analysis_search_filter_list.serialize_json(
            value["filters"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchAnalysesRequest:
    out: SearchAnalysesRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_quicksight.types.analysis_search_filter_list

        out["filters"] = (
            aws_sdk_quicksight.types.analysis_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchAnalysesRequest.filters required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
