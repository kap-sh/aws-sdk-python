"""Generated from Smithy shape ``com.amazonaws.finspace#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.fin_space_taggable_arn


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_finspace.types.fin_space_taggable_arn.FinSpaceTaggableArn"
    """<p>The Amazon Resource Name of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
