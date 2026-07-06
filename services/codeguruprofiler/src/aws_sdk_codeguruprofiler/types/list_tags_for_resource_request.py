"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.profiling_group_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn"
    """<p> The Amazon Resource Name (ARN) of the resource that contains the tags to return. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
