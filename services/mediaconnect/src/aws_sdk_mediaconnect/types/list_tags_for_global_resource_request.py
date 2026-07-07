"""Generated from Smithy shape ``com.amazonaws.mediaconnect#ListTagsForGlobalResourceRequest``."""

from typing_extensions import TypedDict


class ListTagsForGlobalResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the global resource whose tags you want to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForGlobalResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForGlobalResourceRequest:
    out: ListTagsForGlobalResourceRequest = {}  # type: ignore[typeddict-item]
    return out
