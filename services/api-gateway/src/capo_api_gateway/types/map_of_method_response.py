"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfMethodResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.method_response
    import capo_api_gateway.types.string

MapOfMethodResponse: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.method_response.MethodResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfMethodResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_api_gateway.types.method_response

        out[key] = capo_api_gateway.types.method_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfMethodResponse:
    out: MapOfMethodResponse = {}
    for key, value in data.items():
        import capo_api_gateway.types.method_response

        out[key] = capo_api_gateway.types.method_response.deserialize_json(value)
    return out
