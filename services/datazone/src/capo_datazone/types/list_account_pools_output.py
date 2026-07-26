"""Generated from Smithy shape ``com.amazonaws.datazone#ListAccountPoolsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.account_pool_summaries
    import capo_datazone.types.pagination_token


class ListAccountPoolsOutput(TypedDict, closed=True):
    items: NotRequired[
        "capo_datazone.types.account_pool_summaries.AccountPoolSummaries"
    ]
    """<p>The results of the ListAccountPools operation.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of account pools is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of account pools, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListAccountPools to list the next set of account pools.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAccountPoolsOutput) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_datazone.types.account_pool_summaries

        out["items"] = capo_datazone.types.account_pool_summaries.serialize_json(
            value["items"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAccountPoolsOutput:
    out: ListAccountPoolsOutput = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_datazone.types.account_pool_summaries

        out["items"] = capo_datazone.types.account_pool_summaries.deserialize_json(
            data["items"]
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
