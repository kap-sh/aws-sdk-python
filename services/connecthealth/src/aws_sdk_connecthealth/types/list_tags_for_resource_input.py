"""Generated from Smithy shape ``com.amazonaws.connecthealth#ListTagsForResourceInput``."""

from typing import TypedDict


class ListTagsForResourceInput(TypedDict):
    resource_arn: "str"
    """<p>The ARN of the resource to list tags for</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
