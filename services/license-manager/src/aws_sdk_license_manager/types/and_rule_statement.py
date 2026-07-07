"""Generated from Smithy shape ``com.amazonaws.licensemanager#AndRuleStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.matching_rule_statement_list
    import aws_sdk_license_manager.types.script_rule_statement_list


class AndRuleStatement(TypedDict, closed=True):
    matching_rule_statements: NotRequired[
        "aws_sdk_license_manager.types.matching_rule_statement_list.MatchingRuleStatementList"
    ]
    """<p>Matching rule statements.</p>"""
    script_rule_statements: NotRequired[
        "aws_sdk_license_manager.types.script_rule_statement_list.ScriptRuleStatementList"
    ]
    """<p>Script rule statements.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AndRuleStatement) -> dict:
    out: dict = {}
    if "matching_rule_statements" in value:
        import aws_sdk_license_manager.types.matching_rule_statement_list

        out["MatchingRuleStatements"] = (
            aws_sdk_license_manager.types.matching_rule_statement_list.serialize_aws_json_1_1(
                value["matching_rule_statements"]
            )
        )
    if "script_rule_statements" in value:
        import aws_sdk_license_manager.types.script_rule_statement_list

        out["ScriptRuleStatements"] = (
            aws_sdk_license_manager.types.script_rule_statement_list.serialize_aws_json_1_1(
                value["script_rule_statements"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AndRuleStatement:
    out: AndRuleStatement = {}  # type: ignore[typeddict-item]
    if "MatchingRuleStatements" in data:
        import aws_sdk_license_manager.types.matching_rule_statement_list

        out["matching_rule_statements"] = (
            aws_sdk_license_manager.types.matching_rule_statement_list.deserialize_aws_json_1_1(
                data["MatchingRuleStatements"]
            )
        )
    if "ScriptRuleStatements" in data:
        import aws_sdk_license_manager.types.script_rule_statement_list

        out["script_rule_statements"] = (
            aws_sdk_license_manager.types.script_rule_statement_list.deserialize_aws_json_1_1(
                data["ScriptRuleStatements"]
            )
        )
    return out
