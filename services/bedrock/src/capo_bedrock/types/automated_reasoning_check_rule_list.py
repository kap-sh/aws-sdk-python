"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckRuleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_rule

AutomatedReasoningCheckRuleList: TypeAlias = list[
    "capo_bedrock.types.automated_reasoning_check_rule.AutomatedReasoningCheckRule"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckRuleList) -> list:
    import capo_bedrock.types.automated_reasoning_check_rule

    out: list = []
    for item in value:
        out.append(
            capo_bedrock.types.automated_reasoning_check_rule.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutomatedReasoningCheckRuleList:
    import capo_bedrock.types.automated_reasoning_check_rule

    out: AutomatedReasoningCheckRuleList = []
    for item in data:
        out.append(
            capo_bedrock.types.automated_reasoning_check_rule.deserialize_json(item)
        )
    return out
