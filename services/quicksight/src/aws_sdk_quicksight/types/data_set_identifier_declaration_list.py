"""Generated from Smithy shape ``com.amazonaws.quicksight#DataSetIdentifierDeclarationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_set_identifier_declaration

DataSetIdentifierDeclarationList: TypeAlias = list[
    "aws_sdk_quicksight.types.data_set_identifier_declaration.DataSetIdentifierDeclaration"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataSetIdentifierDeclarationList) -> list:
    import aws_sdk_quicksight.types.data_set_identifier_declaration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.data_set_identifier_declaration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataSetIdentifierDeclarationList:
    import aws_sdk_quicksight.types.data_set_identifier_declaration

    out: DataSetIdentifierDeclarationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.data_set_identifier_declaration.deserialize_json(
                item
            )
        )
    return out
