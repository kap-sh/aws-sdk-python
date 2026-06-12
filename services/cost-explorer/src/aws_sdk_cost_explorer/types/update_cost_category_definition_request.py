"""Generated from Smithy shape ``com.amazonaws.costexplorer#UpdateCostCategoryDefinitionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.arn
    import aws_sdk_cost_explorer.types.cost_category_rule_version
    import aws_sdk_cost_explorer.types.cost_category_rules_list
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list
    import aws_sdk_cost_explorer.types.cost_category_value
    import aws_sdk_cost_explorer.types.zoned_date_time


class UpdateCostCategoryDefinitionRequest(TypedDict):
    cost_category_arn: "aws_sdk_cost_explorer.types.arn.Arn"
    """<p>The unique identifier for your cost category.</p>"""
    effective_start: NotRequired[
        "aws_sdk_cost_explorer.types.zoned_date_time.ZonedDateTime"
    ]
    """<p>The cost category's effective start date. It can only be a billing start date (first day of the month). If the date isn't provided, it's the first day of the current month. Dates can't be before the previous twelve months, or in the future.</p>"""
    rule_version: (
        "aws_sdk_cost_explorer.types.cost_category_rule_version.CostCategoryRuleVersion"
    )
    rules: "aws_sdk_cost_explorer.types.cost_category_rules_list.CostCategoryRulesList"
    """<p>The <code>Expression</code> object used to categorize costs. For more information, see <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_CostCategoryRule.html\">CostCategoryRule </a>. </p>"""
    default_value: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]
    split_charge_rules: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.CostCategorySplitChargeRulesList"
    ]
    """<p> The split charge rules used to allocate your charges between your cost category values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCostCategoryDefinitionRequest) -> dict:
    out: dict = {}
    out["CostCategoryArn"] = value["cost_category_arn"]
    if "effective_start" in value:
        out["EffectiveStart"] = value["effective_start"]
    import aws_sdk_cost_explorer.types.cost_category_rule_version

    out["RuleVersion"] = (
        aws_sdk_cost_explorer.types.cost_category_rule_version.serialize_aws_json_1_1(
            value["rule_version"]
        )
    )
    import aws_sdk_cost_explorer.types.cost_category_rules_list

    out["Rules"] = (
        aws_sdk_cost_explorer.types.cost_category_rules_list.serialize_aws_json_1_1(
            value["rules"]
        )
    )
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    if "split_charge_rules" in value:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list

        out["SplitChargeRules"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.serialize_aws_json_1_1(
                value["split_charge_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCostCategoryDefinitionRequest:
    out: UpdateCostCategoryDefinitionRequest = {}  # type: ignore[typeddict-item]
    if "CostCategoryArn" in data:
        out["cost_category_arn"] = data["CostCategoryArn"]
    else:
        raise DeserializationError(
            "UpdateCostCategoryDefinitionRequest.cost_category_arn required"
        )
    if "EffectiveStart" in data:
        out["effective_start"] = data["EffectiveStart"]
    if "RuleVersion" in data:
        import aws_sdk_cost_explorer.types.cost_category_rule_version

        out["rule_version"] = (
            aws_sdk_cost_explorer.types.cost_category_rule_version.deserialize_aws_json_1_1(
                data["RuleVersion"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCostCategoryDefinitionRequest.rule_version required"
        )
    if "Rules" in data:
        import aws_sdk_cost_explorer.types.cost_category_rules_list

        out["rules"] = (
            aws_sdk_cost_explorer.types.cost_category_rules_list.deserialize_aws_json_1_1(
                data["Rules"]
            )
        )
    else:
        raise DeserializationError("UpdateCostCategoryDefinitionRequest.rules required")
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "SplitChargeRules" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list

        out["split_charge_rules"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rules_list.deserialize_aws_json_1_1(
                data["SplitChargeRules"]
            )
        )
    return out
