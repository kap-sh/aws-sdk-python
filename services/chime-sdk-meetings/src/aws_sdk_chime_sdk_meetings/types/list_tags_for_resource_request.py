"""Generated from Smithy shape ``com.amazonaws.chimesdkmeetings#ListTagsForResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_meetings.types.amazon_resource_name


class ListTagsForResourceRequest(TypedDict):
    resource_arn: (
        "aws_sdk_chime_sdk_meetings.types.amazon_resource_name.AmazonResourceName"
    )
    """<p>The ARN of the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceRequest:
    out: ListTagsForResourceRequest = {}  # type: ignore[typeddict-item]
    return out
