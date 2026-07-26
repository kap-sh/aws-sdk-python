"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterOutputSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.media_connect_router_container_settings
    import capo_medialive.types.media_connect_router_output_connection_map
    import capo_medialive.types.output_location_ref


class MediaConnectRouterOutputSettings(TypedDict, closed=True):
    connected_router_inputs: NotRequired[
        "capo_medialive.types.media_connect_router_output_connection_map.MediaConnectRouterOutputConnectionMap"
    ]
    """This parameter is deprecated and unused."""
    container_settings: NotRequired[
        "capo_medialive.types.media_connect_router_container_settings.MediaConnectRouterContainerSettings"
    ]
    destination: NotRequired[
        "capo_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """Destination for this MediaConnect Router Output. The referenced OutputDestination must have MediaConnect Router settings configured."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectRouterOutputSettings) -> dict:
    out: dict = {}
    if "connected_router_inputs" in value:
        import capo_medialive.types.media_connect_router_output_connection_map

        out["connectedRouterInputs"] = (
            capo_medialive.types.media_connect_router_output_connection_map.serialize_json(
                value["connected_router_inputs"]
            )
        )
    if "container_settings" in value:
        import capo_medialive.types.media_connect_router_container_settings

        out["containerSettings"] = (
            capo_medialive.types.media_connect_router_container_settings.serialize_json(
                value["container_settings"]
            )
        )
    if "destination" in value:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    return out


def deserialize_json(data: dict) -> MediaConnectRouterOutputSettings:
    out: MediaConnectRouterOutputSettings = {}  # type: ignore[typeddict-item]
    if "connectedRouterInputs" in data:
        import capo_medialive.types.media_connect_router_output_connection_map

        out["connected_router_inputs"] = (
            capo_medialive.types.media_connect_router_output_connection_map.deserialize_json(
                data["connectedRouterInputs"]
            )
        )
    if "containerSettings" in data:
        import capo_medialive.types.media_connect_router_container_settings

        out["container_settings"] = (
            capo_medialive.types.media_connect_router_container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    if "destination" in data:
        import capo_medialive.types.output_location_ref

        out["destination"] = capo_medialive.types.output_location_ref.deserialize_json(
            data["destination"]
        )
    return out
