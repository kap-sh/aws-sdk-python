"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfEndpointMessageResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.endpoint_message_result

MapOfEndpointMessageResult: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string",
    "capo_pinpoint.types.endpoint_message_result.EndpointMessageResult",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfEndpointMessageResult) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.endpoint_message_result

        out[key] = capo_pinpoint.types.endpoint_message_result.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfEndpointMessageResult:
    out: MapOfEndpointMessageResult = {}
    for key, value in data.items():
        import capo_pinpoint.types.endpoint_message_result

        out[key] = capo_pinpoint.types.endpoint_message_result.deserialize_json(value)
    return out
