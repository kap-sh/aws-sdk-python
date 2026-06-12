"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelDataBinding``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_data_binding_value
    import aws_sdk_iotsitewise.types.computation_model_data_binding_variable

ComputationModelDataBinding: TypeAlias = dict[
    "aws_sdk_iotsitewise.types.computation_model_data_binding_variable.ComputationModelDataBindingVariable",
    "aws_sdk_iotsitewise.types.computation_model_data_binding_value.ComputationModelDataBindingValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComputationModelDataBinding) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iotsitewise.types.computation_model_data_binding_value

        out[key] = (
            aws_sdk_iotsitewise.types.computation_model_data_binding_value.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> ComputationModelDataBinding:
    out: ComputationModelDataBinding = {}
    for key, value in data.items():
        import aws_sdk_iotsitewise.types.computation_model_data_binding_value

        out[key] = (
            aws_sdk_iotsitewise.types.computation_model_data_binding_value.deserialize_json(
                value
            )
        )
    return out
