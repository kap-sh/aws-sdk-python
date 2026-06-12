"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfMethod``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_api_gateway.types.method
    import aws_sdk_api_gateway.types.string

MapOfMethod: TypeAlias = dict[
    "aws_sdk_api_gateway.types.string.String", "aws_sdk_api_gateway.types.method.Method"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfMethod) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_api_gateway.types.method

        out[key] = aws_sdk_api_gateway.types.method.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfMethod:
    out: MapOfMethod = {}
    for key, value in data.items():
        import aws_sdk_api_gateway.types.method

        out[key] = aws_sdk_api_gateway.types.method.deserialize_json(value)
    return out
