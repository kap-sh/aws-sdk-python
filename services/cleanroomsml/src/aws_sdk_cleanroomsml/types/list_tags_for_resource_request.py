"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.taggable_arn


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_cleanroomsml.types.taggable_arn.TaggableArn"
    """<p>The Amazon Resource Name (ARN) of the resource that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
