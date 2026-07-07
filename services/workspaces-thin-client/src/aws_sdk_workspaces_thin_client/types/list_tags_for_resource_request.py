"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ListTagsForResourceRequest``."""

from typing_extensions import TypedDict


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the resource for which you want to retrieve tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
