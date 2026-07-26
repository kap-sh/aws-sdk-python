"""Generated from Smithy shape ``com.amazonaws.apigateway#MapOfMethodSnapshot``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_api_gateway.types.method_snapshot
    import capo_api_gateway.types.string

MapOfMethodSnapshot: TypeAlias = dict[
    "capo_api_gateway.types.string.String",
    "capo_api_gateway.types.method_snapshot.MethodSnapshot",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfMethodSnapshot) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_api_gateway.types.method_snapshot

        out[key] = capo_api_gateway.types.method_snapshot.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfMethodSnapshot:
    out: MapOfMethodSnapshot = {}
    for key, value in data.items():
        import capo_api_gateway.types.method_snapshot

        out[key] = capo_api_gateway.types.method_snapshot.deserialize_json(value)
    return out
