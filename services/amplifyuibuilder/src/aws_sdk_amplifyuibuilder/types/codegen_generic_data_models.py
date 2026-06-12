"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataModels``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_model

CodegenGenericDataModels: TypeAlias = dict["str", "aws_sdk_amplifyuibuilder.types.codegen_generic_data_model.CodegenGenericDataModel"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CodegenGenericDataModels) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_model
        out[key] = aws_sdk_amplifyuibuilder.types.codegen_generic_data_model.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CodegenGenericDataModels:
    out: CodegenGenericDataModels = {}
    for key, value in data.items():
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_model
        out[key] = aws_sdk_amplifyuibuilder.types.codegen_generic_data_model.deserialize_json(value)
    return out