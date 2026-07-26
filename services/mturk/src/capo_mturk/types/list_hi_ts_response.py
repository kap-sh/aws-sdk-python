"""Generated from Smithy shape ``com.amazonaws.mturk#ListHITsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mturk.types.hit_list
    import capo_mturk.types.integer
    import capo_mturk.types.pagination_token


class ListHITsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_mturk.types.pagination_token.PaginationToken"]
    num_results: NotRequired["capo_mturk.types.integer.Integer"]
    """<p>The number of HITs on this page in the filtered results list, equivalent to the number of HITs being returned by this call.</p>"""
    hi_ts: NotRequired["capo_mturk.types.hit_list.HITList"]
    """<p> The list of HIT elements returned by the query.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListHITsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "num_results" in value:
        out["NumResults"] = value["num_results"]
    if "hi_ts" in value:
        import capo_mturk.types.hit_list

        out["HITs"] = capo_mturk.types.hit_list.serialize_aws_json_1_1(value["hi_ts"])
    return out


def deserialize_aws_json_1_1(data: dict) -> ListHITsResponse:
    out: ListHITsResponse = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NumResults" in data:
        out["num_results"] = data["NumResults"]
    if "HITs" in data:
        import capo_mturk.types.hit_list

        out["hi_ts"] = capo_mturk.types.hit_list.deserialize_aws_json_1_1(data["HITs"])
    return out
