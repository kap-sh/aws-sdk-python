"""Generated from Smithy shape ``com.amazonaws.kafka#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string


class ListTagsForResourceRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_kafka.types.__string.__string"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the resource that's associated with the tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
