"""Generated from Smithy shape ``com.amazonaws.frauddetector#ListOfRuleResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.rule_result

ListOfRuleResults: TypeAlias = list[
    "aws_sdk_frauddetector.types.rule_result.RuleResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListOfRuleResults) -> list:
    import aws_sdk_frauddetector.types.rule_result

    out: list = []
    for item in value:
        out.append(aws_sdk_frauddetector.types.rule_result.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ListOfRuleResults:
    import aws_sdk_frauddetector.types.rule_result

    out: ListOfRuleResults = []
    for item in data:
        out.append(
            aws_sdk_frauddetector.types.rule_result.deserialize_aws_json_1_1(item)
        )
    return out
