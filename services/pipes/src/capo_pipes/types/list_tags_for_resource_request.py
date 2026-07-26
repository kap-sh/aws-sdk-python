"""Generated from Smithy shape ``com.amazonaws.pipes#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.pipe_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_pipes.types.pipe_arn.PipeArn"
    """<p>The ARN of the pipe for which you want to view tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
