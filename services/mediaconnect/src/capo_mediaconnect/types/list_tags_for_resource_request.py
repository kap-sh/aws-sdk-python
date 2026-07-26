"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListTagsForResourceRequest``."""

from typing_extensions import TypedDict


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p> The Amazon Resource Name (ARN) that identifies the MediaConnect resource for which to list the tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
