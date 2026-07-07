"""Generated from Smithy shape ``com.amazonaws.lambda#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.taggable_resource


class ListTagsRequest(TypedDict, closed=True):
    resource: "aws_sdk_lambda.types.taggable_resource.TaggableResource"
    """<p>The resource's Amazon Resource Name (ARN). Note: Lambda does not support adding tags to function aliases or versions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    return out
