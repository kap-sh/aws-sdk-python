"""Generated from Smithy shape ``com.amazonaws.workspaces#IpRuleItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.ip_rule
    import aws_sdk_workspaces.types.ip_rule_desc


class IpRuleItem(TypedDict):
    ip_rule: NotRequired["aws_sdk_workspaces.types.ip_rule.IpRule"]
    """<p>The IP address range, in CIDR notation.</p>"""
    rule_desc: NotRequired["aws_sdk_workspaces.types.ip_rule_desc.IpRuleDesc"]
    """<p>The description.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IpRuleItem) -> dict:
    out: dict = {}
    if "ip_rule" in value:
        out["ipRule"] = value["ip_rule"]
    if "rule_desc" in value:
        out["ruleDesc"] = value["rule_desc"]
    return out


def deserialize_aws_json_1_1(data: dict) -> IpRuleItem:
    out: IpRuleItem = {}  # type: ignore[typeddict-item]
    if "ipRule" in data:
        out["ip_rule"] = data["ipRule"]
    if "ruleDesc" in data:
        out["rule_desc"] = data["ruleDesc"]
    return out
