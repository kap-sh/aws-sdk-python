"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IpRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.ip_rule

IpRuleList: TypeAlias = list["aws_sdk_workspaces_web.types.ip_rule.IpRule"]


# --- restJson1 ser/de ---
def serialize_json(value: IpRuleList) -> list:
    import aws_sdk_workspaces_web.types.ip_rule

    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces_web.types.ip_rule.serialize_json(item))
    return out


def deserialize_json(data: list) -> IpRuleList:
    import aws_sdk_workspaces_web.types.ip_rule

    out: IpRuleList = []
    for item in data:
        out.append(aws_sdk_workspaces_web.types.ip_rule.deserialize_json(item))
    return out
