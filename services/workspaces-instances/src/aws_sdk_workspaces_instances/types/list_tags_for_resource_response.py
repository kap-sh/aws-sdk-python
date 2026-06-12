"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#ListTagsForResourceResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.tag_list

class ListTagsForResourceResponse(TypedDict):
    tags: NotRequired["aws_sdk_workspaces_instances.types.tag_list.TagList"]
    """<p>Collection of tags associated with the WorkSpace Instance.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListTagsForResourceResponse) -> dict:
    out: dict = {}
    if "tags" in value:
        import aws_sdk_workspaces_instances.types.tag_list
        out["Tags"] = aws_sdk_workspaces_instances.types.tag_list.serialize_aws_json_1_0(value["tags"])
    return out


def deserialize_aws_json_1_0(data: dict) -> ListTagsForResourceResponse:
    out: ListTagsForResourceResponse = {}  # type: ignore[typeddict-item]
    if "Tags" in data:
        import aws_sdk_workspaces_instances.types.tag_list
        out["tags"] = aws_sdk_workspaces_instances.types.tag_list.deserialize_aws_json_1_0(data["Tags"])
    return out