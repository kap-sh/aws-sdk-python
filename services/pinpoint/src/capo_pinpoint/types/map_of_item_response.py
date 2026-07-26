"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfItemResponse``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.item_response

MapOfItemResponse: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string",
    "capo_pinpoint.types.item_response.ItemResponse",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfItemResponse) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.item_response

        out[key] = capo_pinpoint.types.item_response.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfItemResponse:
    out: MapOfItemResponse = {}
    for key, value in data.items():
        import capo_pinpoint.types.item_response

        out[key] = capo_pinpoint.types.item_response.deserialize_json(value)
    return out
