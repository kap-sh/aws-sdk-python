"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldOptionErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.field_option_error

FieldOptionErrorList: TypeAlias = list[
    "capo_connectcases.types.field_option_error.FieldOptionError"
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldOptionErrorList) -> list:
    import capo_connectcases.types.field_option_error

    out: list = []
    for item in value:
        out.append(capo_connectcases.types.field_option_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldOptionErrorList:
    import capo_connectcases.types.field_option_error

    out: FieldOptionErrorList = []
    for item in data:
        out.append(capo_connectcases.types.field_option_error.deserialize_json(item))
    return out
