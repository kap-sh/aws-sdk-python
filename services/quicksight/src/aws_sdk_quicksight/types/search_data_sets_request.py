"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchDataSetsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.data_set_search_filter_list
    import aws_sdk_quicksight.types.max_results
    import aws_sdk_quicksight.types.string


class SearchDataSetsRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID.</p>"""
    filters: (
        "aws_sdk_quicksight.types.data_set_search_filter_list.DataSetSearchFilterList"
    )
    """<p>The filters to apply to the search.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>A pagination token that can be used in a subsequent request.</p>"""
    max_results: NotRequired["aws_sdk_quicksight.types.max_results.MaxResults"]
    """<p>The maximum number of results to be returned per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchDataSetsRequest) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_set_search_filter_list

    out["Filters"] = (
        aws_sdk_quicksight.types.data_set_search_filter_list.serialize_json(
            value["filters"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> SearchDataSetsRequest:
    out: SearchDataSetsRequest = {}  # type: ignore[typeddict-item]
    if "Filters" in data:
        import aws_sdk_quicksight.types.data_set_search_filter_list

        out["filters"] = (
            aws_sdk_quicksight.types.data_set_search_filter_list.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchDataSetsRequest.filters required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
