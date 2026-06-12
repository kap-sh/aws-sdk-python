"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#CodegenGenericDataEnums``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum

CodegenGenericDataEnums: TypeAlias = dict["str", "aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum.CodegenGenericDataEnum"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CodegenGenericDataEnums) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum
        out[key] = aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum.serialize_json(value)
    return out


def deserialize_json(data: dict) -> CodegenGenericDataEnums:
    out: CodegenGenericDataEnums = {}
    for key, value in data.items():
        import aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum
        out[key] = aws_sdk_amplifyuibuilder.types.codegen_generic_data_enum.deserialize_json(value)
    return out