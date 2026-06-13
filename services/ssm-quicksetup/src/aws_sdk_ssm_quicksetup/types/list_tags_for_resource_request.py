"""Generated from Smithy shape ``com.amazonaws.ssmquicksetup#ListTagsForResourceRequest``."""

from typing import TypedDict


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The ARN of the resource the tag is assigned to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
