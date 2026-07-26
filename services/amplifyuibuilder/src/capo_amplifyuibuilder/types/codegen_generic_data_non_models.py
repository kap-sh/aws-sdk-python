"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataNonModels``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_non_model

CodegenGenericDataNonModels: TypeAlias = dict[
    "str",
    "capo_amplifyuibuilder.types.codegen_generic_data_non_model.CodegenGenericDataNonModel",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CodegenGenericDataNonModels) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_amplifyuibuilder.types.codegen_generic_data_non_model

        out[key] = (
            capo_amplifyuibuilder.types.codegen_generic_data_non_model.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataNonModels:
    out: CodegenGenericDataNonModels = {}
    for key, value in data.items():
        import capo_amplifyuibuilder.types.codegen_generic_data_non_model

        out[key] = (
            capo_amplifyuibuilder.types.codegen_generic_data_non_model.deserialize_json(
                value
            )
        )
    return out
