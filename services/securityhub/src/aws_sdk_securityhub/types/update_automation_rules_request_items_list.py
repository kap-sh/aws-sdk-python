"""Generated from Smithy shape ``com.amazonaws.securityhub#UpdateAutomationRulesRequestItemsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.update_automation_rules_request_item

UpdateAutomationRulesRequestItemsList: TypeAlias = list[
    "aws_sdk_securityhub.types.update_automation_rules_request_item.UpdateAutomationRulesRequestItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAutomationRulesRequestItemsList) -> list:
    import aws_sdk_securityhub.types.update_automation_rules_request_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.update_automation_rules_request_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UpdateAutomationRulesRequestItemsList:
    import aws_sdk_securityhub.types.update_automation_rules_request_item

    out: UpdateAutomationRulesRequestItemsList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.update_automation_rules_request_item.deserialize_json(
                item
            )
        )
    return out
