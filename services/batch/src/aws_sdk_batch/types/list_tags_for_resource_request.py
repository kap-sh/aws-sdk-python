"""Generated from Smithy shape ``com.amazonaws.batch#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_batch.types.string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_batch.types.string.String"
    """<p>The Amazon Resource Name (ARN) that identifies the resource that tags are listed for. Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
