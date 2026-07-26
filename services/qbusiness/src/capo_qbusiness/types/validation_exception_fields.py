"""Generated from Smithy shape ``com.amazonaws.qbusiness#ValidationExceptionFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.validation_exception_field

ValidationExceptionFields: TypeAlias = list[
    "capo_qbusiness.types.validation_exception_field.ValidationExceptionField"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionFields) -> list:
    import capo_qbusiness.types.validation_exception_field

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.validation_exception_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> ValidationExceptionFields:
    import capo_qbusiness.types.validation_exception_field

    out: ValidationExceptionFields = []
    for item in data:
        out.append(
            capo_qbusiness.types.validation_exception_field.deserialize_json(item)
        )
    return out
