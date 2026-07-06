"""Generated from Smithy shape ``com.amazonaws.quicksight#SearchSpacesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.next_token
    import aws_sdk_quicksight.types.space_quicksight_search_filters
    import aws_sdk_quicksight.types.spaces_max_results


class SearchSpacesRequest(TypedDict, closed=True):
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the spaces.</p>"""
    next_token: NotRequired["aws_sdk_quicksight.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no more results.</p>"""
    max_results: "aws_sdk_quicksight.types.spaces_max_results.SpacesMaxResults"
    """<p>The maximum number of results to return.</p>"""
    filters: "aws_sdk_quicksight.types.space_quicksight_search_filters.SpaceQuicksightSearchFilters"
    """<p>The filters to apply to the search.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpacesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value.get("max_results", 100)
    import aws_sdk_quicksight.types.space_quicksight_search_filters

    out["Filters"] = (
        aws_sdk_quicksight.types.space_quicksight_search_filters.serialize_json(
            value["filters"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchSpacesRequest:
    out: SearchSpacesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 100
    if "Filters" in data:
        import aws_sdk_quicksight.types.space_quicksight_search_filters

        out["filters"] = (
            aws_sdk_quicksight.types.space_quicksight_search_filters.deserialize_json(
                data["Filters"]
            )
        )
    else:
        raise DeserializationError("SearchSpacesRequest.filters required")
    return out
