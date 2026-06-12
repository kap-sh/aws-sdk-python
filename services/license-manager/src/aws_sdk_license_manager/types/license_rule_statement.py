"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseRuleStatement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.and_rule_statement
    import aws_sdk_license_manager.types.matching_rule_statement
    import aws_sdk_license_manager.types.or_rule_statement


class LicenseRuleStatement(TypedDict):
    and_rule_statement: NotRequired[
        "aws_sdk_license_manager.types.and_rule_statement.AndRuleStatement"
    ]
    """<p>AND rule statement.</p>"""
    or_rule_statement: NotRequired[
        "aws_sdk_license_manager.types.or_rule_statement.OrRuleStatement"
    ]
    """<p>OR rule statement.</p>"""
    matching_rule_statement: NotRequired[
        "aws_sdk_license_manager.types.matching_rule_statement.MatchingRuleStatement"
    ]
    """<p>Matching rule statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseRuleStatement) -> dict:
    out: dict = {}
    if "and_rule_statement" in value:
        import aws_sdk_license_manager.types.and_rule_statement

        out["AndRuleStatement"] = (
            aws_sdk_license_manager.types.and_rule_statement.serialize_aws_json_1_1(
                value["and_rule_statement"]
            )
        )
    if "or_rule_statement" in value:
        import aws_sdk_license_manager.types.or_rule_statement

        out["OrRuleStatement"] = (
            aws_sdk_license_manager.types.or_rule_statement.serialize_aws_json_1_1(
                value["or_rule_statement"]
            )
        )
    if "matching_rule_statement" in value:
        import aws_sdk_license_manager.types.matching_rule_statement

        out["MatchingRuleStatement"] = (
            aws_sdk_license_manager.types.matching_rule_statement.serialize_aws_json_1_1(
                value["matching_rule_statement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseRuleStatement:
    out: LicenseRuleStatement = {}  # type: ignore[typeddict-item]
    if "AndRuleStatement" in data:
        import aws_sdk_license_manager.types.and_rule_statement

        out["and_rule_statement"] = (
            aws_sdk_license_manager.types.and_rule_statement.deserialize_aws_json_1_1(
                data["AndRuleStatement"]
            )
        )
    if "OrRuleStatement" in data:
        import aws_sdk_license_manager.types.or_rule_statement

        out["or_rule_statement"] = (
            aws_sdk_license_manager.types.or_rule_statement.deserialize_aws_json_1_1(
                data["OrRuleStatement"]
            )
        )
    if "MatchingRuleStatement" in data:
        import aws_sdk_license_manager.types.matching_rule_statement

        out["matching_rule_statement"] = (
            aws_sdk_license_manager.types.matching_rule_statement.deserialize_aws_json_1_1(
                data["MatchingRuleStatement"]
            )
        )
    return out
