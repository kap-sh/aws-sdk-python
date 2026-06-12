"""Generated from Smithy shape ``com.amazonaws.dlm#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dlm.types.policy_arn
    import aws_sdk_dlm.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_dlm.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["aws_sdk_dlm.types.tag_map.TagMap"]
    """<p>One or more tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_dlm.types.tag_map

        out["Tags"] = aws_sdk_dlm.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_dlm.types.tag_map

        out["tags"] = aws_sdk_dlm.types.tag_map.deserialize_json(data["Tags"])
    return out
