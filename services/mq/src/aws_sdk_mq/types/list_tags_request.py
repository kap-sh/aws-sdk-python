"""Generated from Smithy shape ``com.amazonaws.mq#ListTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_mq.types.__string


class ListTagsRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_mq.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsRequest:
    out: ListTagsRequest = {}  # type: ignore[typeddict-item]
    return out
