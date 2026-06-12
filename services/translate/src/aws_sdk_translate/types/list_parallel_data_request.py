"""Generated from Smithy shape ``com.amazonaws.translate#ListParallelDataRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_translate.types.max_results_integer
    import aws_sdk_translate.types.next_token


class ListParallelDataRequest(TypedDict):
    next_token: NotRequired["aws_sdk_translate.types.next_token.NextToken"]
    """<p>A string that specifies the next page of results to return in a paginated response.</p>"""
    max_results: NotRequired[
        "aws_sdk_translate.types.max_results_integer.MaxResultsInteger"
    ]
    """<p>The maximum number of parallel data resources returned for each request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListParallelDataRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListParallelDataRequest:
    out: ListParallelDataRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
