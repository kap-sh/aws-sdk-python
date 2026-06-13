"""Generated from Smithy shape ``com.amazonaws.marketplacedeployment#ListTagsForResourceRequest``."""

from typing import TypedDict


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "str"
    """<p>The Amazon Resource Name (ARN) associated with the deployment parameter resource you want to list tags on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
