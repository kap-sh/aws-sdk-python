"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ValidationExceptionFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.validation_exception_field

ValidationExceptionFieldList: TypeAlias = list[
    "aws_sdk_wellarchitected.types.validation_exception_field.ValidationExceptionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionFieldList) -> list:
    import aws_sdk_wellarchitected.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_wellarchitected.types.validation_exception_field.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ValidationExceptionFieldList:
    import aws_sdk_wellarchitected.types.validation_exception_field

    out: ValidationExceptionFieldList = []
    for item in data:
        out.append(
            aws_sdk_wellarchitected.types.validation_exception_field.deserialize_json(
                item
            )
        )
    return out
