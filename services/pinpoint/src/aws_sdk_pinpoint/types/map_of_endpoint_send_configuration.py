"""Generated from Smithy shape ``com.amazonaws.pinpoint#MapOfEndpointSendConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.endpoint_send_configuration

MapOfEndpointSendConfiguration: TypeAlias = dict[
    "aws_sdk_pinpoint.types.__string.__string",
    "aws_sdk_pinpoint.types.endpoint_send_configuration.EndpointSendConfiguration",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MapOfEndpointSendConfiguration) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_pinpoint.types.endpoint_send_configuration

        out[key] = aws_sdk_pinpoint.types.endpoint_send_configuration.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> MapOfEndpointSendConfiguration:
    out: MapOfEndpointSendConfiguration = {}
    for key, value in data.items():
        import aws_sdk_pinpoint.types.endpoint_send_configuration

        out[key] = aws_sdk_pinpoint.types.endpoint_send_configuration.deserialize_json(
            value
        )
    return out
