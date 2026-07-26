"""Generated from Smithy shape ``com.amazonaws.mgn#CodeGenerationOutputFormatTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.code_generation_output_format_type

CodeGenerationOutputFormatTypes: TypeAlias = list[
    "capo_mgn.types.code_generation_output_format_type.CodeGenerationOutputFormatType"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeGenerationOutputFormatTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> CodeGenerationOutputFormatTypes:
    return list(data)
