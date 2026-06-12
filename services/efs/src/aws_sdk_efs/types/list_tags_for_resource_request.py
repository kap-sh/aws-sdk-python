"""Generated from Smithy shape ``com.amazonaws.efs#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_efs.types.max_results
    import aws_sdk_efs.types.resource_id
    import aws_sdk_efs.types.token


class ListTagsForResourceRequest(TypedDict):
    resource_id: "aws_sdk_efs.types.resource_id.ResourceId"
    """<p>Specifies the EFS resource you want to retrieve tags for. You can retrieve tags for EFS file systems and access points using this API endpoint.</p>"""
    max_results: NotRequired["aws_sdk_efs.types.max_results.MaxResults"]
    """<p>(Optional) Specifies the maximum number of tag objects to return in the response. The default value is 100.</p>"""
    next_token: NotRequired["aws_sdk_efs.types.token.Token"]
    """<p>(Optional) You can use <code>NextToken</code> in a subsequent request to fetch the next page of access point descriptions if the response payload was paginated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
