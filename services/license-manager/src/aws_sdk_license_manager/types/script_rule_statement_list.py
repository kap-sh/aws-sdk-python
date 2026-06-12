"""Generated from Smithy shape ``com.amazonaws.licensemanager#ScriptRuleStatementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.script_rule_statement

ScriptRuleStatementList: TypeAlias = list[
    "aws_sdk_license_manager.types.script_rule_statement.ScriptRuleStatement"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ScriptRuleStatementList) -> list:
    import aws_sdk_license_manager.types.script_rule_statement

    out: list = []
    for item in value:
        out.append(
            aws_sdk_license_manager.types.script_rule_statement.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ScriptRuleStatementList:
    import aws_sdk_license_manager.types.script_rule_statement

    out: ScriptRuleStatementList = []
    for item in data:
        out.append(
            aws_sdk_license_manager.types.script_rule_statement.deserialize_aws_json_1_1(
                item
            )
        )
    return out
