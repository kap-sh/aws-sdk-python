"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.tag_list


class CreateTagsRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, IP access control groups, and connection aliases.</p>"""
    tags: "capo_workspaces.types.tag_list.TagList"
    """<p>The tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateTagsRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_workspaces.types.tag_list

    out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(value["tags"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateTagsRequest:
    out: CreateTagsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("CreateTagsRequest.resource_id required")
    if "Tags" in data:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    else:
        raise DeserializationError("CreateTagsRequest.tags required")
    return out
