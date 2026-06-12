"""Generated from Smithy shape ``com.amazonaws.workspaces#IpRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_rule_item

IpRuleList: TypeAlias = list["aws_sdk_workspaces.types.ip_rule_item.IpRuleItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRuleList) -> list:
    import aws_sdk_workspaces.types.ip_rule_item

    out: list = []
    for item in value:
        out.append(aws_sdk_workspaces.types.ip_rule_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> IpRuleList:
    import aws_sdk_workspaces.types.ip_rule_item

    out: IpRuleList = []
    for item in data:
        out.append(aws_sdk_workspaces.types.ip_rule_item.deserialize_aws_json_1_1(item))
    return out
