"""Generated from Smithy shape ``com.amazonaws.kendra#ListFaqsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.max_results_integer_for_list_faqs_request
    import aws_sdk_kendra.types.next_token


class ListFaqsRequest(TypedDict):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The index for the FAQs.</p>"""
    next_token: NotRequired["aws_sdk_kendra.types.next_token.NextToken"]
    """<p>If the previous response was incomplete (because there is more data to retrieve), Amazon Kendra returns a pagination token in the response. You can use this pagination token to retrieve the next set of FAQs.</p>"""
    max_results: NotRequired[
        "aws_sdk_kendra.types.max_results_integer_for_list_faqs_request.MaxResultsIntegerForListFaqsRequest"
    ]
    """<p>The maximum number of FAQs to return in the response. If there are fewer results in the list, this response contains only the actual results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFaqsRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFaqsRequest:
    out: ListFaqsRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("ListFaqsRequest.index_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
