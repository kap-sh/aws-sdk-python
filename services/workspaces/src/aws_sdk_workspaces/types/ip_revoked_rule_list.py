"""Generated from Smithy shape ``com.amazonaws.workspaces#IpRevokedRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_rule

IpRevokedRuleList: TypeAlias = list["aws_sdk_workspaces.types.ip_rule.IpRule"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRevokedRuleList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> IpRevokedRuleList:
    return list(data)
