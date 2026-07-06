"""Generated from Smithy shape ``com.amazonaws.connect#CreateUserHierarchyGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_id
    import aws_sdk_connect.types.hierarchy_group_name
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.tag_map


class CreateUserHierarchyGroupRequest(TypedDict, closed=True):
    name: "aws_sdk_connect.types.hierarchy_group_name.HierarchyGroupName"
    """<p>The name of the user hierarchy group. Must not be more than 100 characters.</p>"""
    parent_group_id: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier for the parent hierarchy group. The user hierarchy is created at level one if the parent group ID is null.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserHierarchyGroupRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "parent_group_id" in value:
        out["ParentGroupId"] = value["parent_group_id"]
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateUserHierarchyGroupRequest:
    out: CreateUserHierarchyGroupRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateUserHierarchyGroupRequest.name required")
    if "ParentGroupId" in data:
        out["parent_group_id"] = data["ParentGroupId"]
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
