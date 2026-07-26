"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.field_error

BatchGetFieldErrorList: TypeAlias = list[
    "capo_connectcases.types.field_error.FieldError"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldErrorList) -> list:
    import capo_connectcases.types.field_error

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.field_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> BatchGetFieldErrorList:
    import capo_connectcases.types.field_error

    out: BatchGetFieldErrorList = []
    for item in data:
        out.append(capo_connectcases.types.field_error.deserialize_json(item))
    return out
