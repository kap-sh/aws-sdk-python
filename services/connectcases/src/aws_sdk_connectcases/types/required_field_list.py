"""Generated from Smithy shape ``com.amazonaws.connectcases#RequiredFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.required_field

RequiredFieldList: TypeAlias = list[
    "aws_sdk_connectcases.types.required_field.RequiredField"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredFieldList) -> list:
    import aws_sdk_connectcases.types.required_field

    out: list = []
    for item in value:
        out.append(aws_sdk_connectcases.types.required_field.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequiredFieldList:
    import aws_sdk_connectcases.types.required_field

    out: RequiredFieldList = []
    for item in data:
        out.append(aws_sdk_connectcases.types.required_field.deserialize_json(item))
    return out
