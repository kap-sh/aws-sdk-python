"""Generated from Smithy shape ``com.amazonaws.braket#SearchSpendingLimitsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_braket.types.search_spending_limits_filter_list


class SearchSpendingLimitsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to retrieve the next page of results. This value is returned from a previous call to SearchSpendingLimits when there are more results available.</p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 100. Default is 20.</p>"""
    filters: NotRequired[
        "aws_sdk_braket.types.search_spending_limits_filter_list.SearchSpendingLimitsFilterList"
    ]
    """<p>The filters to apply when searching for spending limits. Use filters to narrow down the results based on specific criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSpendingLimitsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import aws_sdk_braket.types.search_spending_limits_filter_list

        out["filters"] = (
            aws_sdk_braket.types.search_spending_limits_filter_list.serialize_json(
                value["filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchSpendingLimitsRequest:
    out: SearchSpendingLimitsRequest = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import aws_sdk_braket.types.search_spending_limits_filter_list

        out["filters"] = (
            aws_sdk_braket.types.search_spending_limits_filter_list.deserialize_json(
                data["filters"]
            )
        )
    return out
