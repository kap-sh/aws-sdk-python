"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfStringToList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.list_of_string
    import aws_sdk_api_gateway.types.string

MapOfStringToList: TypeAlias = dict[
    "aws_sdk_api_gateway.types.string.String",
    "aws_sdk_api_gateway.types.list_of_string.ListOfString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfStringToList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_api_gateway.types.list_of_string

        out[key] = aws_sdk_api_gateway.types.list_of_string.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfStringToList:
    out: MapOfStringToList = {}
    for key, value in data.items():
        import aws_sdk_api_gateway.types.list_of_string

        out[key] = aws_sdk_api_gateway.types.list_of_string.deserialize_json(value)
    return out
