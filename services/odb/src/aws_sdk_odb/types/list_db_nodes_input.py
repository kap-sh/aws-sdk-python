"""Generated from Smithy shape ``com.amazonaws.odb#ListDbNodesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_odb.types.resource_id


class ListDbNodesInput(TypedDict, closed=True):
    max_results: NotRequired["int"]
    """<p>The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output.</p> <p>Default: <code>10</code> </p>"""
    next_token: NotRequired["str"]
    """<p>The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.</p>"""
    cloud_vm_cluster_id: "aws_sdk_odb.types.resource_id.ResourceId"
    """<p>The unique identifier of the VM cluster.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListDbNodesInput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_0(data: dict) -> ListDbNodesInput:
    out: ListDbNodesInput = {}  # type: ignore[typeddict-item]
    return out
