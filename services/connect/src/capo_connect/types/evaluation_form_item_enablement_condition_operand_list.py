"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementConditionOperandList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_condition_operand

EvaluationFormItemEnablementConditionOperandList: TypeAlias = list[
    "capo_connect.types.evaluation_form_item_enablement_condition_operand.EvaluationFormItemEnablementConditionOperand"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementConditionOperandList) -> list:
    import capo_connect.types.evaluation_form_item_enablement_condition_operand

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_item_enablement_condition_operand.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationFormItemEnablementConditionOperandList:
    import capo_connect.types.evaluation_form_item_enablement_condition_operand

    out: EvaluationFormItemEnablementConditionOperandList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_item_enablement_condition_operand.deserialize_json(
                item
            )
        )
    return out
