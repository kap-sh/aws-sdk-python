"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_arn
    import aws_sdk_codeguruprofiler.types.tag_keys


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn"
    """<p> The Amazon Resource Name (ARN) of the resource that contains the tags to remove. </p>"""
    tag_keys: "aws_sdk_codeguruprofiler.types.tag_keys.TagKeys"
    """<p> A list of tag keys. Existing tags of resources with keys in this list are removed from the specified resource. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
