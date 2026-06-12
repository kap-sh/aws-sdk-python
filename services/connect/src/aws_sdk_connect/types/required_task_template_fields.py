"""Generated from Smithy shape ``com.amazonaws.connect#RequiredTaskTemplateFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.required_field_info

RequiredTaskTemplateFields: TypeAlias = list[
    "aws_sdk_connect.types.required_field_info.RequiredFieldInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: RequiredTaskTemplateFields) -> list:
    import aws_sdk_connect.types.required_field_info

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.required_field_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> RequiredTaskTemplateFields:
    import aws_sdk_connect.types.required_field_info

    out: RequiredTaskTemplateFields = []
    for item in data:
        out.append(aws_sdk_connect.types.required_field_info.deserialize_json(item))
    return out
