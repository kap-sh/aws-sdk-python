"""Generated from Smithy shape ``com.amazonaws.quicksight#FilterOperation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.data_set_date_filter_condition
    import capo_quicksight.types.data_set_numeric_filter_condition
    import capo_quicksight.types.data_set_string_filter_condition
    import capo_quicksight.types.expression


class FilterOperation(TypedDict, closed=True):
    condition_expression: NotRequired["capo_quicksight.types.expression.Expression"]
    """<p>An expression that must evaluate to a Boolean value. Rows for which the expression evaluates to true are kept in the dataset.</p>"""
    string_filter_condition: NotRequired[
        "capo_quicksight.types.data_set_string_filter_condition.DataSetStringFilterCondition"
    ]
    """<p>A string-based filter condition within a filter operation.</p>"""
    numeric_filter_condition: NotRequired[
        "capo_quicksight.types.data_set_numeric_filter_condition.DataSetNumericFilterCondition"
    ]
    """<p>A numeric-based filter condition within a filter operation.</p>"""
    date_filter_condition: NotRequired[
        "capo_quicksight.types.data_set_date_filter_condition.DataSetDateFilterCondition"
    ]
    """<p>A date-based filter condition within a filter operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FilterOperation) -> dict:
    out: dict = {}
    if "condition_expression" in value:
        out["ConditionExpression"] = value["condition_expression"]
    if "string_filter_condition" in value:
        import capo_quicksight.types.data_set_string_filter_condition

        out["StringFilterCondition"] = (
            capo_quicksight.types.data_set_string_filter_condition.serialize_json(
                value["string_filter_condition"]
            )
        )
    if "numeric_filter_condition" in value:
        import capo_quicksight.types.data_set_numeric_filter_condition

        out["NumericFilterCondition"] = (
            capo_quicksight.types.data_set_numeric_filter_condition.serialize_json(
                value["numeric_filter_condition"]
            )
        )
    if "date_filter_condition" in value:
        import capo_quicksight.types.data_set_date_filter_condition

        out["DateFilterCondition"] = (
            capo_quicksight.types.data_set_date_filter_condition.serialize_json(
                value["date_filter_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> FilterOperation:
    out: FilterOperation = {}  # type: ignore[typeddict-item]
    if "ConditionExpression" in data:
        out["condition_expression"] = data["ConditionExpression"]
    if "StringFilterCondition" in data:
        import capo_quicksight.types.data_set_string_filter_condition

        out["string_filter_condition"] = (
            capo_quicksight.types.data_set_string_filter_condition.deserialize_json(
                data["StringFilterCondition"]
            )
        )
    if "NumericFilterCondition" in data:
        import capo_quicksight.types.data_set_numeric_filter_condition

        out["numeric_filter_condition"] = (
            capo_quicksight.types.data_set_numeric_filter_condition.deserialize_json(
                data["NumericFilterCondition"]
            )
        )
    if "DateFilterCondition" in data:
        import capo_quicksight.types.data_set_date_filter_condition

        out["date_filter_condition"] = (
            capo_quicksight.types.data_set_date_filter_condition.deserialize_json(
                data["DateFilterCondition"]
            )
        )
    return out
