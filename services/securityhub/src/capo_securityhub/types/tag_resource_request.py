"""Generated from Smithy shape ``com.amazonaws.securityhub#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.resource_arn
    import capo_securityhub.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_securityhub.types.resource_arn.ResourceArn"
    """<p>The ARN of the resource to apply the tags to.</p>"""
    tags: NotRequired["capo_securityhub.types.tag_map.TagMap"]
    """<p>The tags to add to the resource. You can add up to 50 tags at a time. The tag keys can be no longer than 128 characters. The tag values can be no longer than 256 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_securityhub.types.tag_map

        out["Tags"] = capo_securityhub.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_securityhub.types.tag_map

        out["tags"] = capo_securityhub.types.tag_map.deserialize_json(data["Tags"])
    return out
