"""Generated from Smithy shape ``com.amazonaws.inspector2#ValidationExceptionFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.validation_exception_field

ValidationExceptionFields: TypeAlias = list[
    "aws_sdk_inspector2.types.validation_exception_field.ValidationExceptionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionFields) -> list:
    import aws_sdk_inspector2.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.validation_exception_field.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ValidationExceptionFields:
    import aws_sdk_inspector2.types.validation_exception_field

    out: ValidationExceptionFields = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.validation_exception_field.deserialize_json(item)
        )
    return out
