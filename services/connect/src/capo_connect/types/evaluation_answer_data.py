"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswerData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.boolean
    import capo_connect.types.evaluation_answer_data_numeric_value
    import capo_connect.types.evaluation_answer_data_string_value
    import capo_connect.types.evaluation_answer_data_string_value_list
    import capo_connect.types.iso8601_datetime


class _EvaluationAnswerData_StringValue(TypedDict, closed=True):
    StringValue: "capo_connect.types.evaluation_answer_data_string_value.EvaluationAnswerDataStringValue"


class _EvaluationAnswerData_NumericValue(TypedDict, closed=True):
    NumericValue: "capo_connect.types.evaluation_answer_data_numeric_value.EvaluationAnswerDataNumericValue"


class _EvaluationAnswerData_StringValues(TypedDict, closed=True):
    StringValues: "capo_connect.types.evaluation_answer_data_string_value_list.EvaluationAnswerDataStringValueList"


class _EvaluationAnswerData_DateTimeValue(TypedDict, closed=True):
    DateTimeValue: "capo_connect.types.iso8601_datetime.ISO8601Datetime"


class _EvaluationAnswerData_NotApplicable(TypedDict, closed=True):
    NotApplicable: "capo_connect.types.boolean.Boolean"


EvaluationAnswerData: TypeAlias = (
    _EvaluationAnswerData_StringValue
    | _EvaluationAnswerData_NumericValue
    | _EvaluationAnswerData_StringValues
    | _EvaluationAnswerData_DateTimeValue
    | _EvaluationAnswerData_NotApplicable
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationAnswerData) -> dict:
    if "StringValue" in value:
        return {"StringValue": value["StringValue"]}
    elif "NumericValue" in value:
        return {"NumericValue": value["NumericValue"]}
    elif "StringValues" in value:
        import capo_connect.types.evaluation_answer_data_string_value_list

        return {
            "StringValues": capo_connect.types.evaluation_answer_data_string_value_list.serialize_json(
                value["StringValues"]
            )
        }
    elif "DateTimeValue" in value:
        return {"DateTimeValue": value["DateTimeValue"]}
    elif "NotApplicable" in value:
        return {"NotApplicable": value["NotApplicable"]}
    else:
        raise SerializationError("EvaluationAnswerData: no variant present")


def deserialize_json(data: dict) -> EvaluationAnswerData:
    if "StringValue" in data:
        return {"StringValue": data["StringValue"]}
    elif "NumericValue" in data:
        return {"NumericValue": data["NumericValue"]}
    elif "StringValues" in data:
        import capo_connect.types.evaluation_answer_data_string_value_list

        return {
            "StringValues": capo_connect.types.evaluation_answer_data_string_value_list.deserialize_json(
                data["StringValues"]
            )
        }
    elif "DateTimeValue" in data:
        return {"DateTimeValue": data["DateTimeValue"]}
    elif "NotApplicable" in data:
        return {"NotApplicable": data["NotApplicable"]}
    else:
        raise DeserializationError("EvaluationAnswerData: no recognized variant key")
