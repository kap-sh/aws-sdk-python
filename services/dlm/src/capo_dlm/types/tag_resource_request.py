"""Generated from Smithy shape ``com.amazonaws.dlm#TagResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dlm.types.policy_arn
    import capo_dlm.types.tag_map


class TagResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_dlm.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    tags: NotRequired["capo_dlm.types.tag_map.TagMap"]
    """<p>One or more tags.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TagResourceRequest) -> dict:
    out: dict = {}
    if "tags" in value:
        import capo_dlm.types.tag_map

        out["Tags"] = capo_dlm.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> TagResourceRequest:
    out: TagResourceRequest = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import capo_dlm.types.tag_map

        out["tags"] = capo_dlm.types.tag_map.deserialize_json(data["Tags"])
    return out
