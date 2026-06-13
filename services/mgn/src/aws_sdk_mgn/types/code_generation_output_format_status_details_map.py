"""Generated from Smithy shape ``com.amazonaws.mgn#CodeGenerationOutputFormatStatusDetailsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mgn.types.code_generation_output_format_status_details
    import aws_sdk_mgn.types.code_generation_output_format_type

CodeGenerationOutputFormatStatusDetailsMap: TypeAlias = dict[
    "aws_sdk_mgn.types.code_generation_output_format_type.CodeGenerationOutputFormatType",
    "aws_sdk_mgn.types.code_generation_output_format_status_details.CodeGenerationOutputFormatStatusDetails",
]


# --- restJson1 ser/de ---
def serialize_json(
    input_to_serialize: CodeGenerationOutputFormatStatusDetailsMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_mgn.types.code_generation_output_format_status_details

        out[key] = (
            aws_sdk_mgn.types.code_generation_output_format_status_details.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CodeGenerationOutputFormatStatusDetailsMap:
    out: CodeGenerationOutputFormatStatusDetailsMap = {}
    for key, value in data.items():
        import aws_sdk_mgn.types.code_generation_output_format_status_details

        out[key] = (
            aws_sdk_mgn.types.code_generation_output_format_status_details.deserialize_json(
                value
            )
        )
    return out
