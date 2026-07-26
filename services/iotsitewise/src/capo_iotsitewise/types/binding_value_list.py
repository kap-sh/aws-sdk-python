"""Generated from Smithy shape ``com.amazonaws.iotsitewise#BindingValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.computation_model_data_binding_value

BindingValueList: TypeAlias = list[
    "capo_iotsitewise.types.computation_model_data_binding_value.ComputationModelDataBindingValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: BindingValueList) -> list:
    import capo_iotsitewise.types.computation_model_data_binding_value

    out: list = []
    for item in value:
        out.append(
            capo_iotsitewise.types.computation_model_data_binding_value.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BindingValueList:
    import capo_iotsitewise.types.computation_model_data_binding_value

    out: BindingValueList = []
    for item in data:
        out.append(
            capo_iotsitewise.types.computation_model_data_binding_value.deserialize_json(
                item
            )
        )
    return out
