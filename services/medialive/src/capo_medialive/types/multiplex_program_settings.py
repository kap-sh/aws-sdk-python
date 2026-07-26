"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgramSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max65535
    import capo_medialive.types.multiplex_program_service_descriptor
    import capo_medialive.types.multiplex_video_settings
    import capo_medialive.types.preferred_channel_pipeline


class MultiplexProgramSettings(TypedDict, closed=True):
    preferred_channel_pipeline: NotRequired[
        "capo_medialive.types.preferred_channel_pipeline.PreferredChannelPipeline"
    ]
    """Indicates which pipeline is preferred by the multiplex for program ingest."""
    program_number: NotRequired[
        "capo_medialive.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Unique program number."""
    service_descriptor: NotRequired[
        "capo_medialive.types.multiplex_program_service_descriptor.MultiplexProgramServiceDescriptor"
    ]
    """Transport stream service descriptor configuration for the Multiplex program."""
    video_settings: NotRequired[
        "capo_medialive.types.multiplex_video_settings.MultiplexVideoSettings"
    ]
    """Program video settings configuration."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgramSettings) -> dict:
    out: dict = {}
    if "preferred_channel_pipeline" in value:
        import capo_medialive.types.preferred_channel_pipeline

        out["preferredChannelPipeline"] = (
            capo_medialive.types.preferred_channel_pipeline.serialize_json(
                value["preferred_channel_pipeline"]
            )
        )
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "service_descriptor" in value:
        import capo_medialive.types.multiplex_program_service_descriptor

        out["serviceDescriptor"] = (
            capo_medialive.types.multiplex_program_service_descriptor.serialize_json(
                value["service_descriptor"]
            )
        )
    if "video_settings" in value:
        import capo_medialive.types.multiplex_video_settings

        out["videoSettings"] = (
            capo_medialive.types.multiplex_video_settings.serialize_json(
                value["video_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexProgramSettings:
    out: MultiplexProgramSettings = {}  # type: ignore[typeddict-item]
    if "preferredChannelPipeline" in data:
        import capo_medialive.types.preferred_channel_pipeline

        out["preferred_channel_pipeline"] = (
            capo_medialive.types.preferred_channel_pipeline.deserialize_json(
                data["preferredChannelPipeline"]
            )
        )
    if "programNumber" in data:
        out["program_number"] = data["programNumber"]
    if "serviceDescriptor" in data:
        import capo_medialive.types.multiplex_program_service_descriptor

        out["service_descriptor"] = (
            capo_medialive.types.multiplex_program_service_descriptor.deserialize_json(
                data["serviceDescriptor"]
            )
        )
    if "videoSettings" in data:
        import capo_medialive.types.multiplex_video_settings

        out["video_settings"] = (
            capo_medialive.types.multiplex_video_settings.deserialize_json(
                data["videoSettings"]
            )
        )
    return out
