"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfValidationError``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.validation_error

__listOfValidationError: TypeAlias = list[
    "capo_medialive.types.validation_error.ValidationError"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfValidationError) -> list:
    import capo_medialive.types.validation_error

    out: list = []
    for item in value:
        out.append(capo_medialive.types.validation_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfValidationError:
    import capo_medialive.types.validation_error

    out: __listOfValidationError = []
    for item in data:
        out.append(capo_medialive.types.validation_error.deserialize_json(item))
    return out
