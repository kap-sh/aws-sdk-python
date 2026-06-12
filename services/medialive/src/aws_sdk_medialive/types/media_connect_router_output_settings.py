"""Generated from Smithy shape ``com.amazonaws.medialive#MediaConnectRouterOutputSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.media_connect_router_container_settings
    import aws_sdk_medialive.types.media_connect_router_output_connection_map
    import aws_sdk_medialive.types.output_location_ref


class MediaConnectRouterOutputSettings(TypedDict):
    connected_router_inputs: NotRequired[
        "aws_sdk_medialive.types.media_connect_router_output_connection_map.MediaConnectRouterOutputConnectionMap"
    ]
    """This parameter is deprecated and unused."""
    container_settings: NotRequired[
        "aws_sdk_medialive.types.media_connect_router_container_settings.MediaConnectRouterContainerSettings"
    ]
    destination: NotRequired[
        "aws_sdk_medialive.types.output_location_ref.OutputLocationRef"
    ]
    """Destination for this MediaConnect Router Output. The referenced OutputDestination must have MediaConnect Router settings configured."""


# --- restJson1 ser/de ---
def serialize_json(value: MediaConnectRouterOutputSettings) -> dict:
    out: dict = {}
    if "connected_router_inputs" in value:
        import aws_sdk_medialive.types.media_connect_router_output_connection_map

        out["connectedRouterInputs"] = (
            aws_sdk_medialive.types.media_connect_router_output_connection_map.serialize_json(
                value["connected_router_inputs"]
            )
        )
    if "container_settings" in value:
        import aws_sdk_medialive.types.media_connect_router_container_settings

        out["containerSettings"] = (
            aws_sdk_medialive.types.media_connect_router_container_settings.serialize_json(
                value["container_settings"]
            )
        )
    if "destination" in value:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = aws_sdk_medialive.types.output_location_ref.serialize_json(
            value["destination"]
        )
    return out


def deserialize_json(data: dict) -> MediaConnectRouterOutputSettings:
    out: MediaConnectRouterOutputSettings = {}  # type: ignore[typeddict-item]
    if "connectedRouterInputs" in data:
        import aws_sdk_medialive.types.media_connect_router_output_connection_map

        out["connected_router_inputs"] = (
            aws_sdk_medialive.types.media_connect_router_output_connection_map.deserialize_json(
                data["connectedRouterInputs"]
            )
        )
    if "containerSettings" in data:
        import aws_sdk_medialive.types.media_connect_router_container_settings

        out["container_settings"] = (
            aws_sdk_medialive.types.media_connect_router_container_settings.deserialize_json(
                data["containerSettings"]
            )
        )
    if "destination" in data:
        import aws_sdk_medialive.types.output_location_ref

        out["destination"] = (
            aws_sdk_medialive.types.output_location_ref.deserialize_json(
                data["destination"]
            )
        )
    return out
