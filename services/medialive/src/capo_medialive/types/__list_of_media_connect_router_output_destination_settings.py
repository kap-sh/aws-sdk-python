"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfMediaConnectRouterOutputDestinationSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.media_connect_router_output_destination_settings

__listOfMediaConnectRouterOutputDestinationSettings: TypeAlias = list[
    "capo_medialive.types.media_connect_router_output_destination_settings.MediaConnectRouterOutputDestinationSettings"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfMediaConnectRouterOutputDestinationSettings) -> list:
    import capo_medialive.types.media_connect_router_output_destination_settings

    out: list = []
    for item in value:
        out.append(
            capo_medialive.types.media_connect_router_output_destination_settings.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfMediaConnectRouterOutputDestinationSettings:
    import capo_medialive.types.media_connect_router_output_destination_settings

    out: __listOfMediaConnectRouterOutputDestinationSettings = []
    for item in data:
        out.append(
            capo_medialive.types.media_connect_router_output_destination_settings.deserialize_json(
                item
            )
        )
    return out
