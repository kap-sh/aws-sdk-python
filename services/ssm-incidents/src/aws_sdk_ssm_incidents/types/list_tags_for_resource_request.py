"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListTagsForResourceRequest``."""

from typing import TypedDict


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the response plan or incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
