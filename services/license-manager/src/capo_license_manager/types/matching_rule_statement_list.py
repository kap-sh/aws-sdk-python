"""Generated from Smithy shape ``com.amazonaws.licensemanager#MatchingRuleStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_license_manager.types.matching_rule_statement

MatchingRuleStatementList: TypeAlias = list[
    "capo_license_manager.types.matching_rule_statement.MatchingRuleStatement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MatchingRuleStatementList) -> list:
    import capo_license_manager.types.matching_rule_statement

    out: list = []
    for item in value:
        out.append(
            capo_license_manager.types.matching_rule_statement.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MatchingRuleStatementList:
    import capo_license_manager.types.matching_rule_statement

    out: MatchingRuleStatementList = []
    for item in data:
        out.append(
            capo_license_manager.types.matching_rule_statement.deserialize_aws_json_1_1(
                item
            )
        )
    return out
