"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.boolean_condition
    import capo_connect.types.date_time_condition
    import capo_connect.types.decimal_condition
    import capo_connect.types.evaluation_search_condition_list
    import capo_connect.types.number_condition
    import capo_connect.types.string_condition


class EvaluationSearchCriteria(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.evaluation_search_condition_list.EvaluationSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an OR condition.</p>"""
    and_conditions: NotRequired[
        "capo_connect.types.evaluation_search_condition_list.EvaluationSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an AND condition.</p>"""
    string_condition: NotRequired["capo_connect.types.string_condition.StringCondition"]
    number_condition: NotRequired["capo_connect.types.number_condition.NumberCondition"]
    boolean_condition: NotRequired[
        "capo_connect.types.boolean_condition.BooleanCondition"
    ]
    """<p>The boolean condition search criteria for searching evaluations.</p>"""
    date_time_condition: NotRequired[
        "capo_connect.types.date_time_condition.DateTimeCondition"
    ]
    """<p>The datetime condition search criteria for searching evaluations.</p>"""
    decimal_condition: NotRequired[
        "capo_connect.types.decimal_condition.DecimalCondition"
    ]
    """<p>The decimal condition search criteria for searching evaluations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.evaluation_search_condition_list

        out["OrConditions"] = (
            capo_connect.types.evaluation_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import capo_connect.types.evaluation_search_condition_list

        out["AndConditions"] = (
            capo_connect.types.evaluation_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import capo_connect.types.string_condition

        out["StringCondition"] = capo_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "number_condition" in value:
        import capo_connect.types.number_condition

        out["NumberCondition"] = capo_connect.types.number_condition.serialize_json(
            value["number_condition"]
        )
    if "boolean_condition" in value:
        import capo_connect.types.boolean_condition

        out["BooleanCondition"] = capo_connect.types.boolean_condition.serialize_json(
            value["boolean_condition"]
        )
    if "date_time_condition" in value:
        import capo_connect.types.date_time_condition

        out["DateTimeCondition"] = (
            capo_connect.types.date_time_condition.serialize_json(
                value["date_time_condition"]
            )
        )
    if "decimal_condition" in value:
        import capo_connect.types.decimal_condition

        out["DecimalCondition"] = capo_connect.types.decimal_condition.serialize_json(
            value["decimal_condition"]
        )
    return out


def deserialize_json(data: dict) -> EvaluationSearchCriteria:
    out: EvaluationSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import capo_connect.types.evaluation_search_condition_list

        out["or_conditions"] = (
            capo_connect.types.evaluation_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import capo_connect.types.evaluation_search_condition_list

        out["and_conditions"] = (
            capo_connect.types.evaluation_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import capo_connect.types.string_condition

        out["string_condition"] = capo_connect.types.string_condition.deserialize_json(
            data["StringCondition"]
        )
    if "NumberCondition" in data:
        import capo_connect.types.number_condition

        out["number_condition"] = capo_connect.types.number_condition.deserialize_json(
            data["NumberCondition"]
        )
    if "BooleanCondition" in data:
        import capo_connect.types.boolean_condition

        out["boolean_condition"] = (
            capo_connect.types.boolean_condition.deserialize_json(
                data["BooleanCondition"]
            )
        )
    if "DateTimeCondition" in data:
        import capo_connect.types.date_time_condition

        out["date_time_condition"] = (
            capo_connect.types.date_time_condition.deserialize_json(
                data["DateTimeCondition"]
            )
        )
    if "DecimalCondition" in data:
        import capo_connect.types.decimal_condition

        out["decimal_condition"] = (
            capo_connect.types.decimal_condition.deserialize_json(
                data["DecimalCondition"]
            )
        )
    return out
