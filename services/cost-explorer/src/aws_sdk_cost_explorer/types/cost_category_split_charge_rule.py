"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_split_charge_method
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameters_list
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_targets_list
    import aws_sdk_cost_explorer.types.generic_string


class CostCategorySplitChargeRule(TypedDict):
    source: "aws_sdk_cost_explorer.types.generic_string.GenericString"
    """<p>The cost category value that you want to split. That value can't be used as a source or a target in other split charge rules. To indicate uncategorized costs, you can use an empty string as the source.</p>"""
    targets: "aws_sdk_cost_explorer.types.cost_category_split_charge_rule_targets_list.CostCategorySplitChargeRuleTargetsList"
    """<p>The cost category values that you want to split costs across. These values can't be used as a source in other split charge rules. </p>"""
    method: "aws_sdk_cost_explorer.types.cost_category_split_charge_method.CostCategorySplitChargeMethod"
    """<p>The method that's used to define how to split your source costs across your targets. </p> <p> <code>Proportional</code> - Allocates charges across your targets based on the proportional weighted cost of each target.</p> <p> <code>Fixed</code> - Allocates charges across your targets based on your defined allocation percentage.</p> <p>><code>Even</code> - Allocates costs evenly across all targets.</p>"""
    parameters: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameters_list.CostCategorySplitChargeRuleParametersList"
    ]
    """<p>The parameters for a split charge method. This is only required for the <code>FIXED</code> method. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRule) -> dict:
    out: dict = {}
    out["Source"] = value["source"]
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_targets_list

    out["Targets"] = (
        aws_sdk_cost_explorer.types.cost_category_split_charge_rule_targets_list.serialize_aws_json_1_1(
            value["targets"]
        )
    )
    import aws_sdk_cost_explorer.types.cost_category_split_charge_method

    out["Method"] = (
        aws_sdk_cost_explorer.types.cost_category_split_charge_method.serialize_aws_json_1_1(
            value["method"]
        )
    )
    if "parameters" in value:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameters_list

        out["Parameters"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameters_list.serialize_aws_json_1_1(
                value["parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategorySplitChargeRule:
    out: CostCategorySplitChargeRule = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("CostCategorySplitChargeRule.source required")
    if "Targets" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_targets_list

        out["targets"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rule_targets_list.deserialize_aws_json_1_1(
                data["Targets"]
            )
        )
    else:
        raise DeserializationError("CostCategorySplitChargeRule.targets required")
    if "Method" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_method

        out["method"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_method.deserialize_aws_json_1_1(
                data["Method"]
            )
        )
    else:
        raise DeserializationError("CostCategorySplitChargeRule.method required")
    if "Parameters" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameters_list

        out["parameters"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameters_list.deserialize_aws_json_1_1(
                data["Parameters"]
            )
        )
    return out
