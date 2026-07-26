"""Generated from Smithy shape ``com.amazonaws.licensemanager#InstanceRuleStatement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.and_rule_statement
    import capo_license_manager.types.matching_rule_statement
    import capo_license_manager.types.or_rule_statement
    import capo_license_manager.types.script_rule_statement


class InstanceRuleStatement(TypedDict, closed=True):
    and_rule_statement: NotRequired[
        "capo_license_manager.types.and_rule_statement.AndRuleStatement"
    ]
    """<p>AND rule statement.</p>"""
    or_rule_statement: NotRequired[
        "capo_license_manager.types.or_rule_statement.OrRuleStatement"
    ]
    """<p>OR rule statement.</p>"""
    matching_rule_statement: NotRequired[
        "capo_license_manager.types.matching_rule_statement.MatchingRuleStatement"
    ]
    """<p>Matching rule statement.</p>"""
    script_rule_statement: NotRequired[
        "capo_license_manager.types.script_rule_statement.ScriptRuleStatement"
    ]
    """<p>Script rule statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InstanceRuleStatement) -> dict:
    out: dict = {}
    if "and_rule_statement" in value:
        import capo_license_manager.types.and_rule_statement

        out["AndRuleStatement"] = (
            capo_license_manager.types.and_rule_statement.serialize_aws_json_1_1(
                value["and_rule_statement"]
            )
        )
    if "or_rule_statement" in value:
        import capo_license_manager.types.or_rule_statement

        out["OrRuleStatement"] = (
            capo_license_manager.types.or_rule_statement.serialize_aws_json_1_1(
                value["or_rule_statement"]
            )
        )
    if "matching_rule_statement" in value:
        import capo_license_manager.types.matching_rule_statement

        out["MatchingRuleStatement"] = (
            capo_license_manager.types.matching_rule_statement.serialize_aws_json_1_1(
                value["matching_rule_statement"]
            )
        )
    if "script_rule_statement" in value:
        import capo_license_manager.types.script_rule_statement

        out["ScriptRuleStatement"] = (
            capo_license_manager.types.script_rule_statement.serialize_aws_json_1_1(
                value["script_rule_statement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InstanceRuleStatement:
    out: InstanceRuleStatement = {}  # type: ignore[typeddict-item]
    if "AndRuleStatement" in data:
        import capo_license_manager.types.and_rule_statement

        out["and_rule_statement"] = (
            capo_license_manager.types.and_rule_statement.deserialize_aws_json_1_1(
                data["AndRuleStatement"]
            )
        )
    if "OrRuleStatement" in data:
        import capo_license_manager.types.or_rule_statement

        out["or_rule_statement"] = (
            capo_license_manager.types.or_rule_statement.deserialize_aws_json_1_1(
                data["OrRuleStatement"]
            )
        )
    if "MatchingRuleStatement" in data:
        import capo_license_manager.types.matching_rule_statement

        out["matching_rule_statement"] = (
            capo_license_manager.types.matching_rule_statement.deserialize_aws_json_1_1(
                data["MatchingRuleStatement"]
            )
        )
    if "ScriptRuleStatement" in data:
        import capo_license_manager.types.script_rule_statement

        out["script_rule_statement"] = (
            capo_license_manager.types.script_rule_statement.deserialize_aws_json_1_1(
                data["ScriptRuleStatement"]
            )
        )
    return out
