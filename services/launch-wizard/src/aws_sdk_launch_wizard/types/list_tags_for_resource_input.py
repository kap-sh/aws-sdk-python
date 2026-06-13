"""Generated from Smithy shape ``com.amazonaws.launchwizard#ListTagsForResourceInput``."""

from typing import TypedDict


class ListTagsForResourceInput(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
