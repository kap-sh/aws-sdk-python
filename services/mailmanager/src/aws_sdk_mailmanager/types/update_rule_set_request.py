"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateRuleSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.rule_set_id
    import aws_sdk_mailmanager.types.rule_set_name
    import aws_sdk_mailmanager.types.rules


class UpdateRuleSetRequest(TypedDict, closed=True):
    rule_set_id: "aws_sdk_mailmanager.types.rule_set_id.RuleSetId"
    """<p>The identifier of a rule set you want to update.</p>"""
    rule_set_name: NotRequired["aws_sdk_mailmanager.types.rule_set_name.RuleSetName"]
    """<p>A user-friendly name for the rule set resource.</p>"""
    rules: NotRequired["aws_sdk_mailmanager.types.rules.Rules"]
    """<p>A new set of rules to replace the current rules of the rule set—these rules will override all the rules of the rule set.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRuleSetRequest) -> dict:
    out: dict = {}
    out["RuleSetId"] = value["rule_set_id"]
    if "rule_set_name" in value:
        out["RuleSetName"] = value["rule_set_name"]
    if "rules" in value:
        import aws_sdk_mailmanager.types.rules

        out["Rules"] = aws_sdk_mailmanager.types.rules.serialize_aws_json_1_0(
            value["rules"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRuleSetRequest:
    out: UpdateRuleSetRequest = {}  # type: ignore[typeddict-item]
    if "RuleSetId" in data:
        out["rule_set_id"] = data["RuleSetId"]
    else:
        raise DeserializationError("UpdateRuleSetRequest.rule_set_id required")
    if "RuleSetName" in data:
        out["rule_set_name"] = data["RuleSetName"]
    if "Rules" in data:
        import aws_sdk_mailmanager.types.rules

        out["rules"] = aws_sdk_mailmanager.types.rules.deserialize_aws_json_1_0(
            data["Rules"]
        )
    return out
