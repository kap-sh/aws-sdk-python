"""Generated from Smithy shape ``com.amazonaws.panorama#ValidationExceptionErrorArgumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.validation_exception_error_argument

ValidationExceptionErrorArgumentList: TypeAlias = list[
    "aws_sdk_panorama.types.validation_exception_error_argument.ValidationExceptionErrorArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidationExceptionErrorArgumentList) -> list:
    import aws_sdk_panorama.types.validation_exception_error_argument

    out: list = []
    for item in value:
        out.append(
            aws_sdk_panorama.types.validation_exception_error_argument.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ValidationExceptionErrorArgumentList:
    import aws_sdk_panorama.types.validation_exception_error_argument

    out: ValidationExceptionErrorArgumentList = []
    for item in data:
        out.append(
            aws_sdk_panorama.types.validation_exception_error_argument.deserialize_json(
                item
            )
        )
    return out
