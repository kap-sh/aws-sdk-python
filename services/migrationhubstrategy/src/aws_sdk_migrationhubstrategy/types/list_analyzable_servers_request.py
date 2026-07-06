"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ListAnalyzableServersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.max_result
    import aws_sdk_migrationhubstrategy.types.next_token
    import aws_sdk_migrationhubstrategy.types.sort_order


class ListAnalyzableServersRequest(TypedDict, closed=True):
    sort: NotRequired["aws_sdk_migrationhubstrategy.types.sort_order.SortOrder"]
    """Specifies whether to sort by ascending (ASC) or descending (DESC) order."""
    next_token: NotRequired["aws_sdk_migrationhubstrategy.types.next_token.NextToken"]
    """The token from a previous call that you use to retrieve the next set of results. For example, if a previous call to this action returned 100 items, but you set maxResults to 10. You'll receive a set of 10 results along with a token. You then use the returned token to retrieve the next set of 10."""
    max_results: NotRequired["aws_sdk_migrationhubstrategy.types.max_result.MaxResult"]
    """The maximum number of items to include in the response. The maximum value is 100."""


# --- restJson1 ser/de ---
def serialize_json(value: ListAnalyzableServersRequest) -> dict:
    out: dict = {}
    if "sort" in value:
        out["sort"] = value["sort"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> ListAnalyzableServersRequest:
    out: ListAnalyzableServersRequest = {}  # type: ignore[typeddict-item]
    if "sort" in data:
        out["sort"] = data["sort"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    return out
