"""Generated from Smithy shape ``com.amazonaws.workspaces#DeleteTagsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.non_empty_string
    import capo_workspaces.types.tag_key_list


class DeleteTagsRequest(TypedDict, closed=True):
    resource_id: "capo_workspaces.types.non_empty_string.NonEmptyString"
    """<p>The identifier of the WorkSpaces resource. The supported resource types are WorkSpaces, registered directories, images, custom bundles, IP access control groups, and connection aliases.</p>"""
    tag_keys: "capo_workspaces.types.tag_key_list.TagKeyList"
    """<p>The tag keys.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTagsRequest) -> dict:
    out: dict = {}
    out["ResourceId"] = value["resource_id"]
    import capo_workspaces.types.tag_key_list

    out["TagKeys"] = capo_workspaces.types.tag_key_list.serialize_aws_json_1_1(
        value["tag_keys"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTagsRequest:
    out: DeleteTagsRequest = {}  # type: ignore[typeddict-item]
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("DeleteTagsRequest.resource_id required")
    if "TagKeys" in data:
        import capo_workspaces.types.tag_key_list

        out["tag_keys"] = capo_workspaces.types.tag_key_list.deserialize_aws_json_1_1(
            data["TagKeys"]
        )
    else:
        raise DeserializationError("DeleteTagsRequest.tag_keys required")
    return out
