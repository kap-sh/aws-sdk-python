"""Generated from Smithy shape ``com.amazonaws.connectcases#FieldOptionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.field_option

FieldOptionsList: TypeAlias = list[
    "aws_sdk_connectcases.types.field_option.FieldOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: FieldOptionsList) -> list:
    import aws_sdk_connectcases.types.field_option

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.field_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> FieldOptionsList:
    import aws_sdk_connectcases.types.field_option

    out: FieldOptionsList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.field_option.deserialize_json(item))
    return out
