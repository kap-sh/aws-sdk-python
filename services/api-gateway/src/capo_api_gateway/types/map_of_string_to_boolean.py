"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfStringToBoolean``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.nullable_boolean
    import capo_api_gateway.types.string

MapOfStringToBoolean: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.nullable_boolean.NullableBoolean",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfStringToBoolean) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> MapOfStringToBoolean:
    out: MapOfStringToBoolean = {}
    for key, value in data.items():
        out[key] = value
    return out
