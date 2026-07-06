"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#TagSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_instances.types.resource_type_enum
    import aws_sdk_workspaces_instances.types.tag_list


class TagSpecification(TypedDict, closed=True):
    resource_type: NotRequired[
        "aws_sdk_workspaces_instances.types.resource_type_enum.ResourceTypeEnum"
    ]
    """<p>Type of resource being tagged.</p>"""
    tags: NotRequired["aws_sdk_workspaces_instances.types.tag_list.TagList"]
    """<p>Collection of tags for the specified resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TagSpecification) -> dict:
    out: dict = {}
    if "resource_type" in value:
        import aws_sdk_workspaces_instances.types.resource_type_enum

        out["ResourceType"] = (
            aws_sdk_workspaces_instances.types.resource_type_enum.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "tags" in value:
        import aws_sdk_workspaces_instances.types.tag_list

        out["Tags"] = (
            aws_sdk_workspaces_instances.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TagSpecification:
    out: TagSpecification = {}  # type: ignore[typeddict-item]
    if "ResourceType" in data:
        import aws_sdk_workspaces_instances.types.resource_type_enum

        out["resource_type"] = (
            aws_sdk_workspaces_instances.types.resource_type_enum.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if "Tags" in data:
        import aws_sdk_workspaces_instances.types.tag_list

        out["tags"] = (
            aws_sdk_workspaces_instances.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
