"""Generated from Smithy shape ``com.amazonaws.panorama#ValidationExceptionErrorArgumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_panorama.types.validation_exception_error_argument

ValidationExceptionErrorArgumentList: TypeAlias = list[
    "capo_panorama.types.validation_exception_error_argument.ValidationExceptionErrorArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionErrorArgumentList) -> list:
    import capo_panorama.types.validation_exception_error_argument

    out: list = []
    for item in value:
        out.append(
            capo_panorama.types.validation_exception_error_argument.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ValidationExceptionErrorArgumentList:
    import capo_panorama.types.validation_exception_error_argument

    out: ValidationExceptionErrorArgumentList = []
    for item in data:
        out.append(
            capo_panorama.types.validation_exception_error_argument.deserialize_json(
                item
            )
        )
    return out
