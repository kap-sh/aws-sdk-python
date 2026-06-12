"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementConditionOperand``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.evaluation_form_item_enablement_condition
    import aws_sdk_connect.types.evaluation_form_item_enablement_expression


class _EvaluationFormItemEnablementConditionOperand_Expression(TypedDict):
    Expression: "aws_sdk_connect.types.evaluation_form_item_enablement_expression.EvaluationFormItemEnablementExpression"


class _EvaluationFormItemEnablementConditionOperand_Condition(TypedDict):
    Condition: "aws_sdk_connect.types.evaluation_form_item_enablement_condition.EvaluationFormItemEnablementCondition"


EvaluationFormItemEnablementConditionOperand: TypeAlias = (
    _EvaluationFormItemEnablementConditionOperand_Expression
    | _EvaluationFormItemEnablementConditionOperand_Condition
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementConditionOperand) -> dict:
    if "Expression" in value:
        import aws_sdk_connect.types.evaluation_form_item_enablement_expression

        return {
            "Expression": aws_sdk_connect.types.evaluation_form_item_enablement_expression.serialize_json(
                value["Expression"]
            )
        }
    elif "Condition" in value:
        import aws_sdk_connect.types.evaluation_form_item_enablement_condition

        return {
            "Condition": aws_sdk_connect.types.evaluation_form_item_enablement_condition.serialize_json(
                value["Condition"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormItemEnablementConditionOperand: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormItemEnablementConditionOperand:
    if "Expression" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_expression

        return {
            "Expression": aws_sdk_connect.types.evaluation_form_item_enablement_expression.deserialize_json(
                data["Expression"]
            )
        }
    elif "Condition" in data:
        import aws_sdk_connect.types.evaluation_form_item_enablement_condition

        return {
            "Condition": aws_sdk_connect.types.evaluation_form_item_enablement_condition.deserialize_json(
                data["Condition"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementConditionOperand: no recognized variant key"
        )
