"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfRuleResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_frauddetector.types.rule_result

ListOfRuleResults: TypeAlias = list["capo_frauddetector.types.rule_result.RuleResult"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfRuleResults) -> list:
    import capo_frauddetector.types.rule_result

    out: list = []
    for item in value:
        out.append(capo_frauddetector.types.rule_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfRuleResults:
    import capo_frauddetector.types.rule_result

    out: ListOfRuleResults = []
    for item in data:
        out.append(capo_frauddetector.types.rule_result.deserialize_aws_json_1_1(item))
    return out
