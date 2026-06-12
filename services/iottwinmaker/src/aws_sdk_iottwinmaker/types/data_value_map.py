"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DataValueMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.data_value
    import aws_sdk_iottwinmaker.types.string

DataValueMap: TypeAlias = dict[
    "aws_sdk_iottwinmaker.types.string.String",
    "aws_sdk_iottwinmaker.types.data_value.DataValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: DataValueMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_iottwinmaker.types.data_value

        out[key] = aws_sdk_iottwinmaker.types.data_value.serialize_json(value)
    return out


def deserialize_json(data: dict) -> DataValueMap:
    out: DataValueMap = {}
    for key, value in data.items():
        import aws_sdk_iottwinmaker.types.data_value

        out[key] = aws_sdk_iottwinmaker.types.data_value.deserialize_json(value)
    return out
