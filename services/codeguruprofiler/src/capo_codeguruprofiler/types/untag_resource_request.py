"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UntagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.profiling_group_arn
    import capo_codeguruprofiler.types.tag_keys


class UntagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn"
    """<p> The Amazon Resource Name (ARN) of the resource that contains the tags to remove. </p>"""
    tag_keys: "capo_codeguruprofiler.types.tag_keys.TagKeys"
    """<p> A list of tag keys. Existing tags of resources with keys in this list are removed from the specified resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
