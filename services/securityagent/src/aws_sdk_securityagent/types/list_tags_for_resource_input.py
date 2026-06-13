"""Generated from Smithy shape ``com.amazonaws.securityagent#ListTagsForResourceInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityagent.types.resource_arn


class ListTagsForResourceInput(TypedDict):
    resource_arn: "aws_sdk_securityagent.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource to list tags for.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTagsForResourceInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTagsForResourceInput:
    out: ListTagsForResourceInput = {}  # type: ignore[typeddict-item]
    return out
