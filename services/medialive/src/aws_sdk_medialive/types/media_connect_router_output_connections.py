"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterOutputConnections``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.media_connect_router_output_connection

MediaConnectRouterOutputConnections: TypeAlias = dict[
    "aws_sdk_medialive.types.__string.__string",
    "aws_sdk_medialive.types.media_connect_router_output_connection.MediaConnectRouterOutputConnection",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: MediaConnectRouterOutputConnections) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_medialive.types.media_connect_router_output_connection

        out[key] = (
            aws_sdk_medialive.types.media_connect_router_output_connection.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> MediaConnectRouterOutputConnections:
    out: MediaConnectRouterOutputConnections = {}
    for key, value in data.items():
        import aws_sdk_medialive.types.media_connect_router_output_connection

        out[key] = (
            aws_sdk_medialive.types.media_connect_router_output_connection.deserialize_json(
                value
            )
        )
    return out
