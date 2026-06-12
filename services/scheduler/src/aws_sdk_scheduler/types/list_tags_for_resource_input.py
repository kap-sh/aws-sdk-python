"""Generated from Smithy shape ``com.amazonaws.scheduler#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_scheduler.types.tag_resource_arn


class ListTagsForResourceInput(TypedDict):
    resource_arn: "aws_sdk_scheduler.types.tag_resource_arn.TagResourceArn"
    """<p>The ARN of the EventBridge Scheduler resource for which you want to view tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
