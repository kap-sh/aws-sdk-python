"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#ListAutomationRulesResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.automation_rules
    import aws_sdk_compute_optimizer_automation.types.next_token


class ListAutomationRulesResponse(TypedDict):
    automation_rules: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.automation_rules.AutomationRules"
    ]
    """<p> The list of automation rules that match the specified criteria. </p>"""
    next_token: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.next_token.NextToken"
    ]
    """<p>A token used for pagination. If present, indicates there are more results available and can be used in subsequent requests.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAutomationRulesResponse) -> dict:
    out: dict = {}
    if "automation_rules" in value:
        import aws_sdk_compute_optimizer_automation.types.automation_rules

        out["automationRules"] = (
            aws_sdk_compute_optimizer_automation.types.automation_rules.serialize_aws_json_1_0(
                value["automation_rules"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAutomationRulesResponse:
    out: ListAutomationRulesResponse = {}  # type: ignore[typeddict-item]
    if "automationRules" in data:
        import aws_sdk_compute_optimizer_automation.types.automation_rules

        out["automation_rules"] = (
            aws_sdk_compute_optimizer_automation.types.automation_rules.deserialize_aws_json_1_0(
                data["automationRules"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
