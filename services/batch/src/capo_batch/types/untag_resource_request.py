"""Generated from Smithy shape ``com.amazonaws.batch#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_batch.types.string
    import capo_batch.types.tag_keys_list


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_batch.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the resource from which to delete tags. Batch resources that support tags are compute environments, jobs, job definitions, job queues, and scheduling policies. ARNs for child jobs of array and multi-node parallel (MNP) jobs aren't supported.</p>"""
    tag_keys: NotRequired["capo_batch.types.tag_keys_list.TagKeysList"]
    """<p>The keys of the tags to be removed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
