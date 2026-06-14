"""Generated from Smithy shape ``com.amazonaws.appintegrations#ObjectConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_appintegrations.types.non_blank_string
    import aws_sdk_appintegrations.types.fields_map

ObjectConfiguration: TypeAlias = dict["aws_sdk_appintegrations.types.non_blank_string.NonBlankString", "aws_sdk_appintegrations.types.fields_map.FieldsMap"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ObjectConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_appintegrations.types.fields_map
        out[key] = aws_sdk_appintegrations.types.fields_map.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ObjectConfiguration:
    out: ObjectConfiguration = {}
    for key, value in data.items():
        import aws_sdk_appintegrations.types.fields_map
        out[key] = aws_sdk_appintegrations.types.fields_map.deserialize_json(value)
    return out