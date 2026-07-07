"""Generated from Smithy shape ``com.amazonaws.kendra#ListIndicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kendra.types.max_results_integer_for_list_indices_request
    import aws_sdk_kendra.types.next_token


class ListIndicesRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of indexes. </p>"""
    max_results: NotRequired[
        "aws_sdk_kendra.types.max_results_integer_for_list_indices_request.MaxResultsIntegerForListIndicesRequest"
    ]
    """<p>The maximum number of indices to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIndicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIndicesRequest:
    out: ListIndicesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
