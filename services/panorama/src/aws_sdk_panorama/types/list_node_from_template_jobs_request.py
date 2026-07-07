"""Generated from Smithy shape ``com.amazonaws.panorama#ListNodeFromTemplateJobsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_panorama.types.max_size25
    import aws_sdk_panorama.types.next_token


class ListNodeFromTemplateJobsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_panorama.types.next_token.NextToken"]
    """<p>Specify the pagination token from a previous request to retrieve the next page of results.</p>"""
    max_results: "aws_sdk_panorama.types.max_size25.MaxSize25"
    """<p>The maximum number of node from template jobs to return in one page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNodeFromTemplateJobsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListNodeFromTemplateJobsRequest:
    out: ListNodeFromTemplateJobsRequest = {}  # type: ignore[typeddict-item]
    return out
