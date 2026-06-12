"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategorySplitChargeRuleParameter``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cost_explorer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_type
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list


class CostCategorySplitChargeRuleParameter(TypedDict):
    type: "aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_type.CostCategorySplitChargeRuleParameterType"
    """<p>The parameter type. </p>"""
    values: "aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list.CostCategorySplitChargeRuleParameterValuesList"
    """<p>The parameter values. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategorySplitChargeRuleParameter) -> dict:
    out: dict = {}
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_type

    out["Type"] = (
        aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_type.serialize_aws_json_1_1(
            value["type"]
        )
    )
    import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list

    out["Values"] = (
        aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategorySplitChargeRuleParameter:
    out: CostCategorySplitChargeRuleParameter = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_type

        out["type"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("CostCategorySplitChargeRuleParameter.type required")
    if "Values" in data:
        import aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list

        out["values"] = (
            aws_sdk_cost_explorer.types.cost_category_split_charge_rule_parameter_values_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError(
            "CostCategorySplitChargeRuleParameter.values required"
        )
    return out
