"""Generated from Smithy shape ``com.amazonaws.quicksight#ParameterDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.parameter_declaration

ParameterDeclarationList: TypeAlias = list[
    "aws_sdk_quicksight.types.parameter_declaration.ParameterDeclaration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterDeclarationList) -> list:
    import aws_sdk_quicksight.types.parameter_declaration

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.parameter_declaration.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParameterDeclarationList:
    import aws_sdk_quicksight.types.parameter_declaration

    out: ParameterDeclarationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.parameter_declaration.deserialize_json(item)
        )
    return out
