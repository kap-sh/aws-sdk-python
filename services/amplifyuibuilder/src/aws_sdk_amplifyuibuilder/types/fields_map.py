"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#FieldsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_amplifyuibuilder.types.field_config

FieldsMap: TypeAlias = dict[
    "str", "aws_sdk_amplifyuibuilder.types.field_config.FieldConfig"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FieldsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_amplifyuibuilder.types.field_config

        out[key] = aws_sdk_amplifyuibuilder.types.field_config.serialize_json(value)
    return out


def deserialize_json(data: dict) -> FieldsMap:
    out: FieldsMap = {}
    for key, value in data.items():
        import aws_sdk_amplifyuibuilder.types.field_config

        out[key] = aws_sdk_amplifyuibuilder.types.field_config.deserialize_json(value)
    return out
