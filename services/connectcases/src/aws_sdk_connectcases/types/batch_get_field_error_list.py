"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_error

BatchGetFieldErrorList: TypeAlias = list[
    "aws_sdk_connectcases.types.field_error.FieldError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldErrorList) -> list:
    import aws_sdk_connectcases.types.field_error

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.field_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetFieldErrorList:
    import aws_sdk_connectcases.types.field_error

    out: BatchGetFieldErrorList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.field_error.deserialize_json(item))
    return out
