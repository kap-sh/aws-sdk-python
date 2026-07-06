"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesIpGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_group_desc
    import aws_sdk_workspaces.types.ip_group_id
    import aws_sdk_workspaces.types.ip_group_name
    import aws_sdk_workspaces.types.ip_rule_list


class WorkspacesIpGroup(TypedDict, closed=True):
    group_id: NotRequired["aws_sdk_workspaces.types.ip_group_id.IpGroupId"]
    """<p>The identifier of the group.</p>"""
    group_name: NotRequired["aws_sdk_workspaces.types.ip_group_name.IpGroupName"]
    """<p>The name of the group.</p>"""
    group_desc: NotRequired["aws_sdk_workspaces.types.ip_group_desc.IpGroupDesc"]
    """<p>The description of the group.</p>"""
    user_rules: NotRequired["aws_sdk_workspaces.types.ip_rule_list.IpRuleList"]
    """<p>The rules.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspacesIpGroup) -> dict:
    out: dict = {}
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    if "group_name" in value:
        out["groupName"] = value["group_name"]
    if "group_desc" in value:
        out["groupDesc"] = value["group_desc"]
    if "user_rules" in value:
        import aws_sdk_workspaces.types.ip_rule_list

        out["userRules"] = aws_sdk_workspaces.types.ip_rule_list.serialize_aws_json_1_1(
            value["user_rules"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkspacesIpGroup:
    out: WorkspacesIpGroup = {}  # type: ignore[typeddict-item]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    if "groupName" in data:
        out["group_name"] = data["groupName"]
    if "groupDesc" in data:
        out["group_desc"] = data["groupDesc"]
    if "userRules" in data:
        import aws_sdk_workspaces.types.ip_rule_list

        out["user_rules"] = (
            aws_sdk_workspaces.types.ip_rule_list.deserialize_aws_json_1_1(
                data["userRules"]
            )
        )
    return out
