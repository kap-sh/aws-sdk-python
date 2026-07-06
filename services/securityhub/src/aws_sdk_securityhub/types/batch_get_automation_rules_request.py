"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchGetAutomationRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_arns_list


class BatchGetAutomationRulesRequest(TypedDict, closed=True):
    automation_rules_arns: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList"
    ]
    """<p> A list of rule ARNs to get details for. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAutomationRulesRequest) -> dict:
    out: dict = {}
    if "automation_rules_arns" in value:
        import aws_sdk_securityhub.types.automation_rules_arns_list

        out["AutomationRulesArns"] = (
            aws_sdk_securityhub.types.automation_rules_arns_list.serialize_json(
                value["automation_rules_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetAutomationRulesRequest:
    out: BatchGetAutomationRulesRequest = {}  # type: ignore[typeddict-item]
    if "AutomationRulesArns" in data:
        import aws_sdk_securityhub.types.automation_rules_arns_list

        out["automation_rules_arns"] = (
            aws_sdk_securityhub.types.automation_rules_arns_list.deserialize_json(
                data["AutomationRulesArns"]
            )
        )
    return out
