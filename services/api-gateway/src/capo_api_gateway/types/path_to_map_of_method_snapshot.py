"""Generated from Smithy shape ``com.amazonaws.apigateway#PathToMapOfMethodSnapshot``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.map_of_method_snapshot
    import capo_api_gateway.types.string

PathToMapOfMethodSnapshot: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.map_of_method_snapshot.MapOfMethodSnapshot",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PathToMapOfMethodSnapshot) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_api_gateway.types.map_of_method_snapshot

        out[key] = capo_api_gateway.types.map_of_method_snapshot.serialize_json(value)
    return out


def deserialize_json(data: dict) -> PathToMapOfMethodSnapshot:
    out: PathToMapOfMethodSnapshot = {}
    for key, value in data.items():
        import capo_api_gateway.types.map_of_method_snapshot

        out[key] = capo_api_gateway.types.map_of_method_snapshot.deserialize_json(value)
    return out
