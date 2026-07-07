"""Generated from Smithy shape ``com.amazonaws.securityhub#ListAutomationRulesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_metadata_list
    import aws_sdk_securityhub.types.next_token


class ListAutomationRulesResponse(TypedDict, closed=True):
    automation_rules_metadata: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_metadata_list.AutomationRulesMetadataList"
    ]
    """<p> Metadata for rules in the calling account. The response includes rules with a <code>RuleStatus</code> of <code>ENABLED</code> and <code>DISABLED</code>. </p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p> A pagination token for the response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAutomationRulesResponse) -> dict:
    out: dict = {}
    if "automation_rules_metadata" in value:
        import aws_sdk_securityhub.types.automation_rules_metadata_list

        out["AutomationRulesMetadata"] = (
            aws_sdk_securityhub.types.automation_rules_metadata_list.serialize_json(
                value["automation_rules_metadata"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAutomationRulesResponse:
    out: ListAutomationRulesResponse = {}  # type: ignore[typeddict-item]
    if "AutomationRulesMetadata" in data:
        import aws_sdk_securityhub.types.automation_rules_metadata_list

        out["automation_rules_metadata"] = (
            aws_sdk_securityhub.types.automation_rules_metadata_list.deserialize_json(
                data["AutomationRulesMetadata"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
