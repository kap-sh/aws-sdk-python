"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfKeyUsages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.list_of_usage
    import capo_api_gateway.types.string

MapOfKeyUsages: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.list_of_usage.ListOfUsage",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfKeyUsages) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_api_gateway.types.list_of_usage

        out[key] = capo_api_gateway.types.list_of_usage.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfKeyUsages:
    out: MapOfKeyUsages = {}
    for key, value in data.items():
        import capo_api_gateway.types.list_of_usage

        out[key] = capo_api_gateway.types.list_of_usage.deserialize_json(value)
    return out
