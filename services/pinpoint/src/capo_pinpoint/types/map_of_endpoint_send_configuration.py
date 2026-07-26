"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfEndpointSendConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.endpoint_send_configuration

MapOfEndpointSendConfiguration: TypeAlias = dict[
    "capo_pinpoint.types.__string.__string",
    "capo_pinpoint.types.endpoint_send_configuration.EndpointSendConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfEndpointSendConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_pinpoint.types.endpoint_send_configuration

        out[key] = capo_pinpoint.types.endpoint_send_configuration.serialize_json(value)
    return out


def deserialize_json(data: dict) -> MapOfEndpointSendConfiguration:
    out: MapOfEndpointSendConfiguration = {}
    for key, value in data.items():
        import capo_pinpoint.types.endpoint_send_configuration

        out[key] = capo_pinpoint.types.endpoint_send_configuration.deserialize_json(
            value
        )
    return out
