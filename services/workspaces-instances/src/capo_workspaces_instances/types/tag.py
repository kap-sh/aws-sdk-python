"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#Tag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.tag_key
    import capo_workspaces_instances.types.tag_value


class Tag(TypedDict, closed=True):
    key: NotRequired["capo_workspaces_instances.types.tag_key.TagKey"]
    """<p>Unique identifier for the tag.</p>"""
    value: NotRequired["capo_workspaces_instances.types.tag_value.TagValue"]
    """<p>Value associated with the tag key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Tag) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "value" in value:
        out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Tag:
    out: Tag = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Value" in data:
        out["value"] = data["Value"]
    return out
