"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__string


class ListTagsForResourceRequest(TypedDict):
    resource_arn: "aws_sdk_kafkaconnect.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) of the resource for which you want to list all attached tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
