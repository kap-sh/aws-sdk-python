"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserHierarchyGroupNameRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_id
    import aws_sdk_connect.types.hierarchy_group_name
    import aws_sdk_connect.types.instance_id


class UpdateUserHierarchyGroupNameRequest(TypedDict):
    name: "aws_sdk_connect.types.hierarchy_group_name.HierarchyGroupName"
    """<p>The name of the hierarchy group. Must not be more than 100 characters.</p>"""
    hierarchy_group_id: "aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"
    """<p>The identifier of the hierarchy group.</p>"""
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserHierarchyGroupNameRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> UpdateUserHierarchyGroupNameRequest:
    out: UpdateUserHierarchyGroupNameRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateUserHierarchyGroupNameRequest.name required")
    return out
