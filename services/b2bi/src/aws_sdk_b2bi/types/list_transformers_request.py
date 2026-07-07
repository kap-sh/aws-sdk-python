"""Generated from Smithy shape ``com.amazonaws.b2bi#ListTransformersRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_b2bi.types.max_results
    import aws_sdk_b2bi.types.page_token


class ListTransformersRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_b2bi.types.page_token.PageToken"]
    """<p>When additional results are obtained from the command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional resources.</p>"""
    max_results: NotRequired["aws_sdk_b2bi.types.max_results.MaxResults"]
    """<p>Specifies the number of items to return for the API response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTransformersRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTransformersRequest:
    out: ListTransformersRequest = {}  # type: ignore[typeddict-item]
    return out
