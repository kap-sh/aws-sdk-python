"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexOutputDestination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.multiplex_media_connect_output_destination_settings


class MultiplexOutputDestination(TypedDict):
    media_connect_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_media_connect_output_destination_settings.MultiplexMediaConnectOutputDestinationSettings"
    ]
    """Multiplex MediaConnect output destination settings."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexOutputDestination) -> dict:
    out: dict = {}
    if "media_connect_settings" in value:
        import aws_sdk_medialive.types.multiplex_media_connect_output_destination_settings

        out["mediaConnectSettings"] = (
            aws_sdk_medialive.types.multiplex_media_connect_output_destination_settings.serialize_json(
                value["media_connect_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexOutputDestination:
    out: MultiplexOutputDestination = {}  # type: ignore[typeddict-item]
    if "mediaConnectSettings" in data:
        import aws_sdk_medialive.types.multiplex_media_connect_output_destination_settings

        out["media_connect_settings"] = (
            aws_sdk_medialive.types.multiplex_media_connect_output_destination_settings.deserialize_json(
                data["mediaConnectSettings"]
            )
        )
    return out
