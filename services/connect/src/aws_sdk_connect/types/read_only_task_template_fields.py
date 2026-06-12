"""Generated from Smithy shape ``com.amazonaws.connect#ReadOnlyTaskTemplateFields``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.read_only_field_info

ReadOnlyTaskTemplateFields: TypeAlias = list[
    "aws_sdk_connect.types.read_only_field_info.ReadOnlyFieldInfo"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReadOnlyTaskTemplateFields) -> list:
    import aws_sdk_connect.types.read_only_field_info

    out: list = []
    for item in value:
        out.append(aws_sdk_connect.types.read_only_field_info.serialize_json(item))
    return out


def deserialize_json(data: list) -> ReadOnlyTaskTemplateFields:
    import aws_sdk_connect.types.read_only_field_info

    out: ReadOnlyTaskTemplateFields = []
    for item in data:
        out.append(aws_sdk_connect.types.read_only_field_info.deserialize_json(item))
    return out
