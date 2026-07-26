"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementConditionOperand``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_condition
    import capo_connect.types.evaluation_form_item_enablement_expression


class _EvaluationFormItemEnablementConditionOperand_Expression(TypedDict, closed=True):
    Expression: "capo_connect.types.evaluation_form_item_enablement_expression.EvaluationFormItemEnablementExpression"


class _EvaluationFormItemEnablementConditionOperand_Condition(TypedDict, closed=True):
    Condition: "capo_connect.types.evaluation_form_item_enablement_condition.EvaluationFormItemEnablementCondition"


EvaluationFormItemEnablementConditionOperand: TypeAlias = (
    _EvaluationFormItemEnablementConditionOperand_Expression
    | _EvaluationFormItemEnablementConditionOperand_Condition
)


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementConditionOperand) -> dict:
    if "Expression" in value:
        import capo_connect.types.evaluation_form_item_enablement_expression

        return {
            "Expression": capo_connect.types.evaluation_form_item_enablement_expression.serialize_json(
                value["Expression"]
            )
        }
    elif "Condition" in value:
        import capo_connect.types.evaluation_form_item_enablement_condition

        return {
            "Condition": capo_connect.types.evaluation_form_item_enablement_condition.serialize_json(
                value["Condition"]
            )
        }
    else:
        raise SerializationError(
            "EvaluationFormItemEnablementConditionOperand: no variant present"
        )


def deserialize_json(data: dict) -> EvaluationFormItemEnablementConditionOperand:
    if "Expression" in data:
        import capo_connect.types.evaluation_form_item_enablement_expression

        return {
            "Expression": capo_connect.types.evaluation_form_item_enablement_expression.deserialize_json(
                data["Expression"]
            )
        }
    elif "Condition" in data:
        import capo_connect.types.evaluation_form_item_enablement_condition

        return {
            "Condition": capo_connect.types.evaluation_form_item_enablement_condition.deserialize_json(
                data["Condition"]
            )
        }
    else:
        raise DeserializationError(
            "EvaluationFormItemEnablementConditionOperand: no recognized variant key"
        )
