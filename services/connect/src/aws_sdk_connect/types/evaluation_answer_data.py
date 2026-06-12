"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationAnswerData``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.boolean
    import aws_sdk_connect.types.evaluation_answer_data_numeric_value
    import aws_sdk_connect.types.evaluation_answer_data_string_value
    import aws_sdk_connect.types.evaluation_answer_data_string_value_list
    import aws_sdk_connect.types.iso8601_datetime


class _EvaluationAnswerData_StringValue(TypedDict):
    StringValue: "aws_sdk_connect.types.evaluation_answer_data_string_value.EvaluationAnswerDataStringValue"


class _EvaluationAnswerData_NumericValue(TypedDict):
    NumericValue: "aws_sdk_connect.types.evaluation_answer_data_numeric_value.EvaluationAnswerDataNumericValue"


class _EvaluationAnswerData_StringValues(TypedDict):
    StringValues: "aws_sdk_connect.types.evaluation_answer_data_string_value_list.EvaluationAnswerDataStringValueList"


class _EvaluationAnswerData_DateTimeValue(TypedDict):
    DateTimeValue: "aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"


class _EvaluationAnswerData_NotApplicable(TypedDict):
    NotApplicable: "aws_sdk_connect.types.boolean.Boolean"


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
        import aws_sdk_connect.types.evaluation_answer_data_string_value_list

        return {
            "StringValues": aws_sdk_connect.types.evaluation_answer_data_string_value_list.serialize_json(
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
        import aws_sdk_connect.types.evaluation_answer_data_string_value_list

        return {
            "StringValues": aws_sdk_connect.types.evaluation_answer_data_string_value_list.deserialize_json(
                data["StringValues"]
            )
        }
    elif "DateTimeValue" in data:
        return {"DateTimeValue": data["DateTimeValue"]}
    elif "NotApplicable" in data:
        return {"NotApplicable": data["NotApplicable"]}
    else:
        raise DeserializationError("EvaluationAnswerData: no recognized variant key")
