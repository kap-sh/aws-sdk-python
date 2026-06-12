"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormSearchCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean_condition
    import aws_sdk_connect.types.date_time_condition
    import aws_sdk_connect.types.evaluation_form_search_condition_list
    import aws_sdk_connect.types.number_condition
    import aws_sdk_connect.types.string_condition


class EvaluationFormSearchCriteria(TypedDict):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.evaluation_form_search_condition_list.EvaluationFormSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an OR condition.</p>"""
    and_conditions: NotRequired[
        "aws_sdk_connect.types.evaluation_form_search_condition_list.EvaluationFormSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an AND condition.</p>"""
    string_condition: NotRequired[
        "aws_sdk_connect.types.string_condition.StringCondition"
    ]
    number_condition: NotRequired[
        "aws_sdk_connect.types.number_condition.NumberCondition"
    ]
    boolean_condition: NotRequired[
        "aws_sdk_connect.types.boolean_condition.BooleanCondition"
    ]
    """<p>Boolean search condition.</p>"""
    date_time_condition: NotRequired[
        "aws_sdk_connect.types.date_time_condition.DateTimeCondition"
    ]
    """<p>Datetime search condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.evaluation_form_search_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.evaluation_form_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import aws_sdk_connect.types.evaluation_form_search_condition_list

        out["AndConditions"] = (
            aws_sdk_connect.types.evaluation_form_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import aws_sdk_connect.types.string_condition

        out["StringCondition"] = aws_sdk_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "number_condition" in value:
        import aws_sdk_connect.types.number_condition

        out["NumberCondition"] = aws_sdk_connect.types.number_condition.serialize_json(
            value["number_condition"]
        )
    if "boolean_condition" in value:
        import aws_sdk_connect.types.boolean_condition

        out["BooleanCondition"] = (
            aws_sdk_connect.types.boolean_condition.serialize_json(
                value["boolean_condition"]
            )
        )
    if "date_time_condition" in value:
        import aws_sdk_connect.types.date_time_condition

        out["DateTimeCondition"] = (
            aws_sdk_connect.types.date_time_condition.serialize_json(
                value["date_time_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> EvaluationFormSearchCriteria:
    out: EvaluationFormSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.evaluation_form_search_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.evaluation_form_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import aws_sdk_connect.types.evaluation_form_search_condition_list

        out["and_conditions"] = (
            aws_sdk_connect.types.evaluation_form_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import aws_sdk_connect.types.string_condition

        out["string_condition"] = (
            aws_sdk_connect.types.string_condition.deserialize_json(
                data["StringCondition"]
            )
        )
    if "NumberCondition" in data:
        import aws_sdk_connect.types.number_condition

        out["number_condition"] = (
            aws_sdk_connect.types.number_condition.deserialize_json(
                data["NumberCondition"]
            )
        )
    if "BooleanCondition" in data:
        import aws_sdk_connect.types.boolean_condition

        out["boolean_condition"] = (
            aws_sdk_connect.types.boolean_condition.deserialize_json(
                data["BooleanCondition"]
            )
        )
    if "DateTimeCondition" in data:
        import aws_sdk_connect.types.date_time_condition

        out["date_time_condition"] = (
            aws_sdk_connect.types.date_time_condition.deserialize_json(
                data["DateTimeCondition"]
            )
        )
    return out
