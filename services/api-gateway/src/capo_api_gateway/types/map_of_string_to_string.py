"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfStringToString``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.string

MapOfStringToString: TypeAlias = dict[
    "capo_api_gateway.types.string.String", "capo_api_gateway.types.string.String"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfStringToString) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MapOfStringToString:
    out: MapOfStringToString = {}
    for key, value in data.items():
        out[key] = value
    return out
