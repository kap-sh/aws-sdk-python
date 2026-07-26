"""Generated from Smithy shape ``com.amazonaws.connect#EvaluationFormItemEnablementSourceValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.evaluation_form_item_enablement_source_value

EvaluationFormItemEnablementSourceValueList: TypeAlias = list[
    "capo_connect.types.evaluation_form_item_enablement_source_value.EvaluationFormItemEnablementSourceValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: EvaluationFormItemEnablementSourceValueList) -> list:
    import capo_connect.types.evaluation_form_item_enablement_source_value

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.evaluation_form_item_enablement_source_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> EvaluationFormItemEnablementSourceValueList:
    import capo_connect.types.evaluation_form_item_enablement_source_value

    out: EvaluationFormItemEnablementSourceValueList = []
    for item in data:
        out.append(
            capo_connect.types.evaluation_form_item_enablement_source_value.deserialize_json(
                item
            )
        )
    return out
