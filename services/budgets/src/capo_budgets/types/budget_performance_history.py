"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetPerformanceHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_budgets.types.billing_view_arn
    import capo_budgets.types.budget_name
    import capo_budgets.types.budget_type
    import capo_budgets.types.budgeted_and_actual_amounts_list
    import capo_budgets.types.cost_filters
    import capo_budgets.types.cost_types
    import capo_budgets.types.expression
    import capo_budgets.types.metrics
    import capo_budgets.types.time_unit


class BudgetPerformanceHistory(TypedDict, closed=True):
    budget_name: NotRequired["capo_budgets.types.budget_name.BudgetName"]
    budget_type: NotRequired["capo_budgets.types.budget_type.BudgetType"]
    cost_filters: NotRequired["capo_budgets.types.cost_filters.CostFilters"]
    """<p>The history of the cost filters for a budget during the specified time period.</p>"""
    cost_types: NotRequired["capo_budgets.types.cost_types.CostTypes"]
    """<p>The history of the cost types for a budget during the specified time period.</p>"""
    time_unit: NotRequired["capo_budgets.types.time_unit.TimeUnit"]
    billing_view_arn: NotRequired["capo_budgets.types.billing_view_arn.BillingViewArn"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    budgeted_and_actual_amounts_list: NotRequired[
        "capo_budgets.types.budgeted_and_actual_amounts_list.BudgetedAndActualAmountsList"
    ]
    """<p>A list of amounts of cost or usage that you created budgets for, which are compared to your actual costs or usage.</p>"""
    filter_expression: NotRequired["capo_budgets.types.expression.Expression"]
    """<p>The filtering dimensions for the budget and their corresponding values.</p>"""
    metrics: NotRequired["capo_budgets.types.metrics.Metrics"]
    """<p>The definition for how the budget data is aggregated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BudgetPerformanceHistory) -> dict:
    out: dict = {}
    if "budget_name" in value:
        out["BudgetName"] = value["budget_name"]
    if "budget_type" in value:
        import capo_budgets.types.budget_type

        out["BudgetType"] = capo_budgets.types.budget_type.serialize_aws_json_1_1(
            value["budget_type"]
        )
    if "cost_filters" in value:
        import capo_budgets.types.cost_filters

        out["CostFilters"] = capo_budgets.types.cost_filters.serialize_aws_json_1_1(
            value["cost_filters"]
        )
    if "cost_types" in value:
        import capo_budgets.types.cost_types

        out["CostTypes"] = capo_budgets.types.cost_types.serialize_aws_json_1_1(
            value["cost_types"]
        )
    if "time_unit" in value:
        import capo_budgets.types.time_unit

        out["TimeUnit"] = capo_budgets.types.time_unit.serialize_aws_json_1_1(
            value["time_unit"]
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "budgeted_and_actual_amounts_list" in value:
        import capo_budgets.types.budgeted_and_actual_amounts_list

        out["BudgetedAndActualAmountsList"] = (
            capo_budgets.types.budgeted_and_actual_amounts_list.serialize_aws_json_1_1(
                value["budgeted_and_actual_amounts_list"]
            )
        )
    if "filter_expression" in value:
        import capo_budgets.types.expression

        out["FilterExpression"] = capo_budgets.types.expression.serialize_aws_json_1_1(
            value["filter_expression"]
        )
    if "metrics" in value:
        import capo_budgets.types.metrics

        out["Metrics"] = capo_budgets.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BudgetPerformanceHistory:
    out: BudgetPerformanceHistory = {}  # type: ignore[typeddict-item]
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    if "BudgetType" in data:
        import capo_budgets.types.budget_type

        out["budget_type"] = capo_budgets.types.budget_type.deserialize_aws_json_1_1(
            data["BudgetType"]
        )
    if "CostFilters" in data:
        import capo_budgets.types.cost_filters

        out["cost_filters"] = capo_budgets.types.cost_filters.deserialize_aws_json_1_1(
            data["CostFilters"]
        )
    if "CostTypes" in data:
        import capo_budgets.types.cost_types

        out["cost_types"] = capo_budgets.types.cost_types.deserialize_aws_json_1_1(
            data["CostTypes"]
        )
    if "TimeUnit" in data:
        import capo_budgets.types.time_unit

        out["time_unit"] = capo_budgets.types.time_unit.deserialize_aws_json_1_1(
            data["TimeUnit"]
        )
    if "BillingViewArn" in data:
        out["billing_view_arn"] = data["BillingViewArn"]
    if "BudgetedAndActualAmountsList" in data:
        import capo_budgets.types.budgeted_and_actual_amounts_list

        out["budgeted_and_actual_amounts_list"] = (
            capo_budgets.types.budgeted_and_actual_amounts_list.deserialize_aws_json_1_1(
                data["BudgetedAndActualAmountsList"]
            )
        )
    if "FilterExpression" in data:
        import capo_budgets.types.expression

        out["filter_expression"] = (
            capo_budgets.types.expression.deserialize_aws_json_1_1(
                data["FilterExpression"]
            )
        )
    if "Metrics" in data:
        import capo_budgets.types.metrics

        out["metrics"] = capo_budgets.types.metrics.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    return out
