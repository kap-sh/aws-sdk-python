"""Generated from Smithy shape ``com.amazonaws.configservice#ListStoredQueriesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.limit
    import capo_config_service.types.string


class ListStoredQueriesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The nextToken string returned in a previous request that you use to request the next page of results in a paginated response.</p>"""
    max_results: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of results to be returned with a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListStoredQueriesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListStoredQueriesRequest:
    out: ListStoredQueriesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
