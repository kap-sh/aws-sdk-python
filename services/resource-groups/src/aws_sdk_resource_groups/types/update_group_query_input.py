"""Generated from Smithy shape ``com.amazonaws.resourcegroups#UpdateGroupQueryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resource_groups.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resource_groups.types.group_name
    import aws_sdk_resource_groups.types.group_string
    import aws_sdk_resource_groups.types.resource_query


class UpdateGroupQueryInput(TypedDict, closed=True):
    group_name: NotRequired["aws_sdk_resource_groups.types.group_name.GroupName"]
    """<p>Don't use this parameter. Use <code>Group</code> instead.</p>"""
    group: NotRequired["aws_sdk_resource_groups.types.group_string.GroupString"]
    """<p>The name or the Amazon resource name (ARN) of the resource group to query.</p>"""
    resource_query: "aws_sdk_resource_groups.types.resource_query.ResourceQuery"
    """<p>The resource query to determine which Amazon Web Services resources are members of this resource group.</p> <note> <p>A resource group can contain either a <code>Configuration</code> or a <code>ResourceQuery</code>, but not both.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGroupQueryInput) -> dict:
    out: dict = {}
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group" in value:
        out["Group"] = value["group"]
    import aws_sdk_resource_groups.types.resource_query

    out["ResourceQuery"] = aws_sdk_resource_groups.types.resource_query.serialize_json(
        value["resource_query"]
    )
    return out


def deserialize_json(data: dict) -> UpdateGroupQueryInput:
    out: UpdateGroupQueryInput = {}  # type: ignore[typeddict-item]
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "Group" in data:
        out["group"] = data["Group"]
    if "ResourceQuery" in data:
        import aws_sdk_resource_groups.types.resource_query

        out["resource_query"] = (
            aws_sdk_resource_groups.types.resource_query.deserialize_json(
                data["ResourceQuery"]
            )
        )
    else:
        raise DeserializationError("UpdateGroupQueryInput.resource_query required")
    return out
