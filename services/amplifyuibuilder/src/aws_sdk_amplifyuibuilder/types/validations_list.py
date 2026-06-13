"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#ValidationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.field_validation_configuration

ValidationsList: TypeAlias = list[
    "aws_sdk_amplifyuibuilder.types.field_validation_configuration.FieldValidationConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationsList) -> list:
    import aws_sdk_amplifyuibuilder.types.field_validation_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_amplifyuibuilder.types.field_validation_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ValidationsList:
    import aws_sdk_amplifyuibuilder.types.field_validation_configuration

    out: ValidationsList = []
    for item in data:
        out.append(
            aws_sdk_amplifyuibuilder.types.field_validation_configuration.deserialize_json(
                item
            )
        )
    return out
