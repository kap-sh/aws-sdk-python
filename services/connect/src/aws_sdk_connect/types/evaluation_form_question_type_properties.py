"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormQuestionTypeProperties``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_multi_select_question_properties
    import aws_sdk_connect.types.evaluation_form_numeric_question_properties
    import aws_sdk_connect.types.evaluation_form_single_select_question_properties
    import aws_sdk_connect.types.evaluation_form_text_question_properties


class _EvaluationFormQuestionTypeProperties_Numeric(TypedDict, closed=True):
    Numeric: "aws_sdk_connect.types.evaluation_form_numeric_question_properties.EvaluationFormNumericQuestionProperties"


class _EvaluationFormQuestionTypeProperties_SingleSelect(TypedDict, closed=True):
    SingleSelect: "aws_sdk_connect.types.evaluation_form_single_select_question_properties.EvaluationFormSingleSelectQuestionProperties"


class _EvaluationFormQuestionTypeProperties_Text(TypedDict, closed=True):
    Text: "aws_sdk_connect.types.evaluation_form_text_question_properties.EvaluationFormTextQuestionProperties"


class _EvaluationFormQuestionTypeProperties_MultiSelect(TypedDict, closed=True):
    MultiSelect: "aws_sdk_connect.types.evaluation_form_multi_select_question_properties.EvaluationFormMultiSelectQuestionProperties"


EvaluationFormQuestionTypeProperties: TypeAlias = (
    _EvaluationFormQuestionTypeProperties_Numeric
    | _EvaluationFormQuestionTypeProperties_SingleSelect
    | _EvaluationFormQuestionTypeProperties_Text
    | _EvaluationFormQuestionTypeProperties_MultiSelect
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormQuestionTypeProperties) -> dict:
    if "Numeric" in value:
        import aws_sdk_connect.types.evaluation_form_numeric_question_properties

        return {
            "Numeric": aws_sdk_connect.types.evaluation_form_numeric_question_properties.serialize_json(
                value["Numeric"]
            )
        }
    elif "SingleSelect" in value:
        import aws_sdk_connect.types.evaluation_form_single_select_question_properties

        return {
            "SingleSelect": aws_sdk_connect.types.evaluation_form_single_select_question_properties.serialize_json(
                value["SingleSelect"]
            )
        }
    elif "Text" in value:
        import aws_sdk_connect.types.evaluation_form_text_question_properties

        return {
            "Text": aws_sdk_connect.types.evaluation_form_text_question_properties.serialize_json(
                value["Text"]
            )
        }
    elif "MultiSelect" in value:
        import aws_sdk_connect.types.evaluation_form_multi_select_question_properties

        return {
            "MultiSelect": aws_sdk_connect.types.evaluation_form_multi_select_question_properties.serialize_json(
                value["MultiSelect"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormQuestionTypeProperties: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormQuestionTypeProperties:
    if "Numeric" in data:
        import aws_sdk_connect.types.evaluation_form_numeric_question_properties

        return {
            "Numeric": aws_sdk_connect.types.evaluation_form_numeric_question_properties.deserialize_json(
                data["Numeric"]
            )
        }
    elif "SingleSelect" in data:
        import aws_sdk_connect.types.evaluation_form_single_select_question_properties

        return {
            "SingleSelect": aws_sdk_connect.types.evaluation_form_single_select_question_properties.deserialize_json(
                data["SingleSelect"]
            )
        }
    elif "Text" in data:
        import aws_sdk_connect.types.evaluation_form_text_question_properties

        return {
            "Text": aws_sdk_connect.types.evaluation_form_text_question_properties.deserialize_json(
                data["Text"]
            )
        }
    elif "MultiSelect" in data:
        import aws_sdk_connect.types.evaluation_form_multi_select_question_properties

        return {
            "MultiSelect": aws_sdk_connect.types.evaluation_form_multi_select_question_properties.deserialize_json(
                data["MultiSelect"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationFormQuestionTypeProperties: no recognized variant key"
        )
