"""Generated from Smithy shape ``com.amazonaws.securityhub#TagResourceRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resource_arn
    import aws_sdk_securityhub.types.tag_map


class TagResourceRequest(TypedDict):
    resource_arn: "aws_sdk_securityhub.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to apply the tags to.</p>"""
    tags: NotRequired["aws_sdk_securityhub.types.tag_map.TagMap"]
    """<p>The tags to add to the resource. You can add up to 50 tags at a time. The tag keys can be no longer than 128 characters. The tag values can be no longer than 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_securityhub.types.tag_map

        out["Tags"] = aws_sdk_securityhub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_securityhub.types.tag_map

        out["tags"] = aws_sdk_securityhub.types.tag_map.deserialize_json(data["Tags"])
    return out
