"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#OrganizationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids
    import aws_sdk_compute_optimizer_automation.types.rule_apply_order


class OrganizationConfiguration(TypedDict, closed=True):
    rule_apply_order: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.rule_apply_order.RuleApplyOrder"
    ]
    """<p>Specifies when organization rules should be applied relative to account rules.</p>"""
    account_ids: NotRequired[
        "aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids.OrganizationConfigurationAccountIds"
    ]
    """<p>List of specific Amazon Web Services account IDs where the organization rule should be applied.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OrganizationConfiguration) -> dict:
    out: dict = {}
    if "rule_apply_order" in value:
        import aws_sdk_compute_optimizer_automation.types.rule_apply_order

        out["ruleApplyOrder"] = (
            aws_sdk_compute_optimizer_automation.types.rule_apply_order.serialize_aws_json_1_0(
                value["rule_apply_order"]
            )
        )
    if "account_ids" in value:
        import aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids

        out["accountIds"] = (
            aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids.serialize_aws_json_1_0(
                value["account_ids"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OrganizationConfiguration:
    out: OrganizationConfiguration = {}  # type: ignore[typeddict-item]
    if "ruleApplyOrder" in data:
        import aws_sdk_compute_optimizer_automation.types.rule_apply_order

        out["rule_apply_order"] = (
            aws_sdk_compute_optimizer_automation.types.rule_apply_order.deserialize_aws_json_1_0(
                data["ruleApplyOrder"]
            )
        )
    if "accountIds" in data:
        import aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids

        out["account_ids"] = (
            aws_sdk_compute_optimizer_automation.types.organization_configuration_account_ids.deserialize_aws_json_1_0(
                data["accountIds"]
            )
        )
    return out
