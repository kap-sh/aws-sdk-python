"""Generated from Smithy shape ``com.amazonaws.connect#InvisibleTaskTemplateFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.invisible_field_info

InvisibleTaskTemplateFields: TypeAlias = list[
    "aws_sdk_connect.types.invisible_field_info.InvisibleFieldInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: InvisibleTaskTemplateFields) -> list:
    import aws_sdk_connect.types.invisible_field_info

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.invisible_field_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> InvisibleTaskTemplateFields:
    import aws_sdk_connect.types.invisible_field_info

    out: InvisibleTaskTemplateFields = []
    for item in data:
        out.append(aws_sdk_connect.types.invisible_field_info.deserialize_json(item))
    return out
