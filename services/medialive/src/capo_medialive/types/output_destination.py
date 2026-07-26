"""Generated from Smithy shape ``com.amazonaws.medialive#OutputDestination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__list_of__string
    import capo_medialive.types.__list_of_media_connect_router_output_destination_settings
    import capo_medialive.types.__list_of_media_package_output_destination_settings
    import capo_medialive.types.__list_of_output_destination_settings
    import capo_medialive.types.__list_of_srt_output_destination_settings
    import capo_medialive.types.__string
    import capo_medialive.types.multiplex_program_channel_destination_settings


class OutputDestination(TypedDict, closed=True):
    id: NotRequired["capo_medialive.types.__string.__string"]
    """User-specified id. This is used in an output group or an output."""
    media_package_settings: NotRequired[
        "capo_medialive.types.__list_of_media_package_output_destination_settings.__listOfMediaPackageOutputDestinationSettings"
    ]
    """Destination settings for a MediaPackage output; one destination for both encoders."""
    multiplex_settings: NotRequired[
        "capo_medialive.types.multiplex_program_channel_destination_settings.MultiplexProgramChannelDestinationSettings"
    ]
    """Destination settings for a Multiplex output; one destination for both encoders."""
    settings: NotRequired[
        "capo_medialive.types.__list_of_output_destination_settings.__listOfOutputDestinationSettings"
    ]
    """Destination settings for a standard output; one destination for each redundant encoder."""
    srt_settings: NotRequired[
        "capo_medialive.types.__list_of_srt_output_destination_settings.__listOfSrtOutputDestinationSettings"
    ]
    """SRT settings for an SRT output; one destination for each redundant encoder."""
    logical_interface_names: NotRequired[
        "capo_medialive.types.__list_of__string.__listOf__string"
    ]
    """Optional assignment of an output to a logical interface on the Node. Only applies to on premises channels."""
    media_connect_router_settings: NotRequired[
        "capo_medialive.types.__list_of_media_connect_router_output_destination_settings.__listOfMediaConnectRouterOutputDestinationSettings"
    ]
    """Destination settings for a MediaConnect Router output; one destination for each redundant encoder."""


# --- restJson1 ser/de ---
def serialize_json(value: OutputDestination) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "media_package_settings" in value:
        import capo_medialive.types.__list_of_media_package_output_destination_settings

        out["mediaPackageSettings"] = (
            capo_medialive.types.__list_of_media_package_output_destination_settings.serialize_json(
                value["media_package_settings"]
            )
        )
    if "multiplex_settings" in value:
        import capo_medialive.types.multiplex_program_channel_destination_settings

        out["multiplexSettings"] = (
            capo_medialive.types.multiplex_program_channel_destination_settings.serialize_json(
                value["multiplex_settings"]
            )
        )
    if "settings" in value:
        import capo_medialive.types.__list_of_output_destination_settings

        out["settings"] = (
            capo_medialive.types.__list_of_output_destination_settings.serialize_json(
                value["settings"]
            )
        )
    if "srt_settings" in value:
        import capo_medialive.types.__list_of_srt_output_destination_settings

        out["srtSettings"] = (
            capo_medialive.types.__list_of_srt_output_destination_settings.serialize_json(
                value["srt_settings"]
            )
        )
    if "logical_interface_names" in value:
        import capo_medialive.types.__list_of__string

        out["logicalInterfaceNames"] = (
            capo_medialive.types.__list_of__string.serialize_json(
                value["logical_interface_names"]
            )
        )
    if "media_connect_router_settings" in value:
        import capo_medialive.types.__list_of_media_connect_router_output_destination_settings

        out["mediaConnectRouterSettings"] = (
            capo_medialive.types.__list_of_media_connect_router_output_destination_settings.serialize_json(
                value["media_connect_router_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> OutputDestination:
    out: OutputDestination = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "mediaPackageSettings" in data:
        import capo_medialive.types.__list_of_media_package_output_destination_settings

        out["media_package_settings"] = (
            capo_medialive.types.__list_of_media_package_output_destination_settings.deserialize_json(
                data["mediaPackageSettings"]
            )
        )
    if "multiplexSettings" in data:
        import capo_medialive.types.multiplex_program_channel_destination_settings

        out["multiplex_settings"] = (
            capo_medialive.types.multiplex_program_channel_destination_settings.deserialize_json(
                data["multiplexSettings"]
            )
        )
    if "settings" in data:
        import capo_medialive.types.__list_of_output_destination_settings

        out["settings"] = (
            capo_medialive.types.__list_of_output_destination_settings.deserialize_json(
                data["settings"]
            )
        )
    if "srtSettings" in data:
        import capo_medialive.types.__list_of_srt_output_destination_settings

        out["srt_settings"] = (
            capo_medialive.types.__list_of_srt_output_destination_settings.deserialize_json(
                data["srtSettings"]
            )
        )
    if "logicalInterfaceNames" in data:
        import capo_medialive.types.__list_of__string

        out["logical_interface_names"] = (
            capo_medialive.types.__list_of__string.deserialize_json(
                data["logicalInterfaceNames"]
            )
        )
    if "mediaConnectRouterSettings" in data:
        import capo_medialive.types.__list_of_media_connect_router_output_destination_settings

        out["media_connect_router_settings"] = (
            capo_medialive.types.__list_of_media_connect_router_output_destination_settings.deserialize_json(
                data["mediaConnectRouterSettings"]
            )
        )
    return out
