"""Generated from Smithy shape ``com.amazonaws.deadline#UntagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.string
    import aws_sdk_deadline.types.string_list


class UntagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_deadline.types.string.String"
    """<p>The ARN of the resource to remove the tag from.</p>"""
    tag_keys: "aws_sdk_deadline.types.string_list.StringList"
    """<p>They keys of the tag.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UntagResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UntagResourceRequest:
    out: UntagResourceRequest = {}  # type: ignore[typeddict-item]
    return out
