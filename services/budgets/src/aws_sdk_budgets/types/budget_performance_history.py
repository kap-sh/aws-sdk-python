"""Generated from Smithy shape ``com.amazonaws.budgets#BudgetPerformanceHistory``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_budgets.types.billing_view_arn
    import aws_sdk_budgets.types.budget_name
    import aws_sdk_budgets.types.budget_type
    import aws_sdk_budgets.types.budgeted_and_actual_amounts_list
    import aws_sdk_budgets.types.cost_filters
    import aws_sdk_budgets.types.cost_types
    import aws_sdk_budgets.types.expression
    import aws_sdk_budgets.types.metrics
    import aws_sdk_budgets.types.time_unit


class BudgetPerformanceHistory(TypedDict, closed=True):
    budget_name: NotRequired["aws_sdk_budgets.types.budget_name.BudgetName"]
    budget_type: NotRequired["aws_sdk_budgets.types.budget_type.BudgetType"]
    cost_filters: NotRequired["aws_sdk_budgets.types.cost_filters.CostFilters"]
    """<p>The history of the cost filters for a budget during the specified time period.</p>"""
    cost_types: NotRequired["aws_sdk_budgets.types.cost_types.CostTypes"]
    """<p>The history of the cost types for a budget during the specified time period.</p>"""
    time_unit: NotRequired["aws_sdk_budgets.types.time_unit.TimeUnit"]
    billing_view_arn: NotRequired[
        "aws_sdk_budgets.types.billing_view_arn.BillingViewArn"
    ]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies a specific billing view. The ARN is used to specify which particular billing view you want to interact with or retrieve information from when making API calls related to Amazon Web Services Billing and Cost Management features. The BillingViewArn can be retrieved by calling the ListBillingViews API.</p>"""
    budgeted_and_actual_amounts_list: NotRequired[
        "aws_sdk_budgets.types.budgeted_and_actual_amounts_list.BudgetedAndActualAmountsList"
    ]
    """<p>A list of amounts of cost or usage that you created budgets for, which are compared to your actual costs or usage.</p>"""
    filter_expression: NotRequired["aws_sdk_budgets.types.expression.Expression"]
    """<p>The filtering dimensions for the budget and their corresponding values.</p>"""
    metrics: NotRequired["aws_sdk_budgets.types.metrics.Metrics"]
    """<p>The definition for how the budget data is aggregated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BudgetPerformanceHistory) -> dict:
    out: dict = {}
    if "budget_name" in value:
        out["BudgetName"] = value["budget_name"]
    if "budget_type" in value:
        import aws_sdk_budgets.types.budget_type

        out["BudgetType"] = aws_sdk_budgets.types.budget_type.serialize_aws_json_1_1(
            value["budget_type"]
        )
    if "cost_filters" in value:
        import aws_sdk_budgets.types.cost_filters

        out["CostFilters"] = aws_sdk_budgets.types.cost_filters.serialize_aws_json_1_1(
            value["cost_filters"]
        )
    if "cost_types" in value:
        import aws_sdk_budgets.types.cost_types

        out["CostTypes"] = aws_sdk_budgets.types.cost_types.serialize_aws_json_1_1(
            value["cost_types"]
        )
    if "time_unit" in value:
        import aws_sdk_budgets.types.time_unit

        out["TimeUnit"] = aws_sdk_budgets.types.time_unit.serialize_aws_json_1_1(
            value["time_unit"]
        )
    if "billing_view_arn" in value:
        out["BillingViewArn"] = value["billing_view_arn"]
    if "budgeted_and_actual_amounts_list" in value:
        import aws_sdk_budgets.types.budgeted_and_actual_amounts_list

        out["BudgetedAndActualAmountsList"] = (
            aws_sdk_budgets.types.budgeted_and_actual_amounts_list.serialize_aws_json_1_1(
                value["budgeted_and_actual_amounts_list"]
            )
        )
    if "filter_expression" in value:
        import aws_sdk_budgets.types.expression

        out["FilterExpression"] = (
            aws_sdk_budgets.types.expression.serialize_aws_json_1_1(
                value["filter_expression"]
            )
        )
    if "metrics" in value:
        import aws_sdk_budgets.types.metrics

        out["Metrics"] = aws_sdk_budgets.types.metrics.serialize_aws_json_1_1(
            value["metrics"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BudgetPerformanceHistory:
    out: BudgetPerformanceHistory = {}  # type: ignore[typeddict-item]
    if "BudgetName" in data:
        out["budget_name"] = data["BudgetName"]
    if "BudgetType" in data:
        import aws_sdk_budgets.types.budget_type

        out["budget_type"] = aws_sdk_budgets.types.budget_type.deserialize_aws_json_1_1(
            data["BudgetType"]
        )
    if "CostFilters" in data:
        import aws_sdk_budgets.types.cost_filters

        out["cost_filters"] = (
            aws_sdk_budgets.types.cost_filters.deserialize_aws_json_1_1(
                data["CostFilters"]
            )
        )
    if "CostTypes" in data:
        import aws_sdk_budgets.types.cost_types

        out["cost_types"] = aws_sdk_budgets.types.cost_types.deserialize_aws_json_1_1(
            data["CostTypes"]
        )
    if "TimeUnit" in data:
        import aws_sdk_budgets.types.time_unit

        out["time_unit"] = aws_sdk_budgets.types.time_unit.deserialize_aws_json_1_1(
            data["TimeUnit"]
        )
    if "BillingViewArn" in data:
        out["billing_view_arn"] = data["BillingViewArn"]
    if "BudgetedAndActualAmountsList" in data:
        import aws_sdk_budgets.types.budgeted_and_actual_amounts_list

        out["budgeted_and_actual_amounts_list"] = (
            aws_sdk_budgets.types.budgeted_and_actual_amounts_list.deserialize_aws_json_1_1(
                data["BudgetedAndActualAmountsList"]
            )
        )
    if "FilterExpression" in data:
        import aws_sdk_budgets.types.expression

        out["filter_expression"] = (
            aws_sdk_budgets.types.expression.deserialize_aws_json_1_1(
                data["FilterExpression"]
            )
        )
    if "Metrics" in data:
        import aws_sdk_budgets.types.metrics

        out["metrics"] = aws_sdk_budgets.types.metrics.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    return out
