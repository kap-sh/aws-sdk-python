"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item

EvaluationFormItemsList: TypeAlias = list[
    "capo_connect.types.evaluation_form_item.EvaluationFormItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemsList) -> list:
    import capo_connect.types.evaluation_form_item

    out: list = []
    for item in value:
        out.append(capo_connect.types.evaluation_form_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> EvaluationFormItemsList:
    import capo_connect.types.evaluation_form_item

    out: EvaluationFormItemsList = []
    for item in data:
        out.append(capo_connect.types.evaluation_form_item.deserialize_json(item))
    return out
