"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataNonModelFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplifyuibuilder.types.codegen_generic_data_field

CodegenGenericDataNonModelFields: TypeAlias = dict[
    "str",
    "capo_amplifyuibuilder.types.codegen_generic_data_field.CodegenGenericDataField",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CodegenGenericDataNonModelFields) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_amplifyuibuilder.types.codegen_generic_data_field

        out[key] = (
            capo_amplifyuibuilder.types.codegen_generic_data_field.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> CodegenGenericDataNonModelFields:
    out: CodegenGenericDataNonModelFields = {}
    for key, value in data.items():
        import capo_amplifyuibuilder.types.codegen_generic_data_field

        out[key] = (
            capo_amplifyuibuilder.types.codegen_generic_data_field.deserialize_json(
                value
            )
        )
    return out
