"""Generated from Smithy shape ``com.amazonaws.securityhub#BatchDeleteAutomationRulesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_arns_list


class BatchDeleteAutomationRulesRequest(TypedDict):
    automation_rules_arns: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_arns_list.AutomationRulesArnsList"
    ]
    """<p> A list of Amazon Resource Names (ARNs) for the rules that are to be deleted. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteAutomationRulesRequest) -> dict:
    out: dict = {}
    if "automation_rules_arns" in value:
        import aws_sdk_securityhub.types.automation_rules_arns_list

        out["AutomationRulesArns"] = (
            aws_sdk_securityhub.types.automation_rules_arns_list.serialize_json(
                value["automation_rules_arns"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteAutomationRulesRequest:
    out: BatchDeleteAutomationRulesRequest = {}  # type: ignore[typeddict-item]
    if "AutomationRulesArns" in data:
        import aws_sdk_securityhub.types.automation_rules_arns_list

        out["automation_rules_arns"] = (
            aws_sdk_securityhub.types.automation_rules_arns_list.deserialize_json(
                data["AutomationRulesArns"]
            )
        )
    return out
