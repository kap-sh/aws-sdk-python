"""Generated from Smithy shape ``com.amazonaws.panorama#ConflictExceptionErrorArgumentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_panorama.types.conflict_exception_error_argument

ConflictExceptionErrorArgumentList: TypeAlias = list[
    "aws_sdk_panorama.types.conflict_exception_error_argument.ConflictExceptionErrorArgument"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConflictExceptionErrorArgumentList) -> list:
    import aws_sdk_panorama.types.conflict_exception_error_argument

    out: list = []
    for item in value:
        out.append(
            aws_sdk_panorama.types.conflict_exception_error_argument.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ConflictExceptionErrorArgumentList:
    import aws_sdk_panorama.types.conflict_exception_error_argument

    out: ConflictExceptionErrorArgumentList = []
    for item in data:
        out.append(
            aws_sdk_panorama.types.conflict_exception_error_argument.deserialize_json(
                item
            )
        )
    return out
