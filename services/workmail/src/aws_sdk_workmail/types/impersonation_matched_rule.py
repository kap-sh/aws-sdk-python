"""Generated from Smithy shape ``com.amazonaws.workmail#ImpersonationMatchedRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workmail.types.impersonation_rule_id
    import aws_sdk_workmail.types.impersonation_rule_name


class ImpersonationMatchedRule(TypedDict):
    impersonation_rule_id: NotRequired[
        "aws_sdk_workmail.types.impersonation_rule_id.ImpersonationRuleId"
    ]
    """<p>The ID of the rule that matched the input</p>"""
    name: NotRequired[
        "aws_sdk_workmail.types.impersonation_rule_name.ImpersonationRuleName"
    ]
    """<p>The name of the rule that matched the input.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImpersonationMatchedRule) -> dict:
    out: dict = {}
    if "impersonation_rule_id" in value:
        out["ImpersonationRuleId"] = value["impersonation_rule_id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImpersonationMatchedRule:
    out: ImpersonationMatchedRule = {}  # type: ignore[typeddict-item]
    if "ImpersonationRuleId" in data:
        out["impersonation_rule_id"] = data["ImpersonationRuleId"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
