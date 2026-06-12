"""Generated from Smithy shape ``com.amazonaws.licensemanager#RuleStatement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_license_manager.types.instance_rule_statement
    import aws_sdk_license_manager.types.license_configuration_rule_statement
    import aws_sdk_license_manager.types.license_rule_statement


class RuleStatement(TypedDict):
    license_configuration_rule_statement: NotRequired[
        "aws_sdk_license_manager.types.license_configuration_rule_statement.LicenseConfigurationRuleStatement"
    ]
    """<p>License configuration rule statement.</p>"""
    license_rule_statement: NotRequired[
        "aws_sdk_license_manager.types.license_rule_statement.LicenseRuleStatement"
    ]
    """<p>License rule statement.</p>"""
    instance_rule_statement: NotRequired[
        "aws_sdk_license_manager.types.instance_rule_statement.InstanceRuleStatement"
    ]
    """<p>Instance rule statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleStatement) -> dict:
    out: dict = {}
    if "license_configuration_rule_statement" in value:
        import aws_sdk_license_manager.types.license_configuration_rule_statement

        out["LicenseConfigurationRuleStatement"] = (
            aws_sdk_license_manager.types.license_configuration_rule_statement.serialize_aws_json_1_1(
                value["license_configuration_rule_statement"]
            )
        )
    if "license_rule_statement" in value:
        import aws_sdk_license_manager.types.license_rule_statement

        out["LicenseRuleStatement"] = (
            aws_sdk_license_manager.types.license_rule_statement.serialize_aws_json_1_1(
                value["license_rule_statement"]
            )
        )
    if "instance_rule_statement" in value:
        import aws_sdk_license_manager.types.instance_rule_statement

        out["InstanceRuleStatement"] = (
            aws_sdk_license_manager.types.instance_rule_statement.serialize_aws_json_1_1(
                value["instance_rule_statement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleStatement:
    out: RuleStatement = {}  # type: ignore[typeddict-item]
    if "LicenseConfigurationRuleStatement" in data:
        import aws_sdk_license_manager.types.license_configuration_rule_statement

        out["license_configuration_rule_statement"] = (
            aws_sdk_license_manager.types.license_configuration_rule_statement.deserialize_aws_json_1_1(
                data["LicenseConfigurationRuleStatement"]
            )
        )
    if "LicenseRuleStatement" in data:
        import aws_sdk_license_manager.types.license_rule_statement

        out["license_rule_statement"] = (
            aws_sdk_license_manager.types.license_rule_statement.deserialize_aws_json_1_1(
                data["LicenseRuleStatement"]
            )
        )
    if "InstanceRuleStatement" in data:
        import aws_sdk_license_manager.types.instance_rule_statement

        out["instance_rule_statement"] = (
            aws_sdk_license_manager.types.instance_rule_statement.deserialize_aws_json_1_1(
                data["InstanceRuleStatement"]
            )
        )
    return out
