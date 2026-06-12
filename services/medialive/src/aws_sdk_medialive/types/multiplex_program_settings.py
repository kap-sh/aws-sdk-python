"""Generated from Smithy shape ``com.amazonaws.medialive#MultiplexProgramSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0_max65535
    import aws_sdk_medialive.types.multiplex_program_service_descriptor
    import aws_sdk_medialive.types.multiplex_video_settings
    import aws_sdk_medialive.types.preferred_channel_pipeline


class MultiplexProgramSettings(TypedDict):
    preferred_channel_pipeline: NotRequired[
        "aws_sdk_medialive.types.preferred_channel_pipeline.PreferredChannelPipeline"
    ]
    """Indicates which pipeline is preferred by the multiplex for program ingest."""
    program_number: NotRequired[
        "aws_sdk_medialive.types.__integer_min0_max65535.__integerMin0Max65535"
    ]
    """Unique program number."""
    service_descriptor: NotRequired[
        "aws_sdk_medialive.types.multiplex_program_service_descriptor.MultiplexProgramServiceDescriptor"
    ]
    """Transport stream service descriptor configuration for the Multiplex program."""
    video_settings: NotRequired[
        "aws_sdk_medialive.types.multiplex_video_settings.MultiplexVideoSettings"
    ]
    """Program video settings configuration."""


# --- restJson1 ser/de ---
def serialize_json(value: MultiplexProgramSettings) -> dict:
    out: dict = {}
    if "preferred_channel_pipeline" in value:
        import aws_sdk_medialive.types.preferred_channel_pipeline

        out["preferredChannelPipeline"] = (
            aws_sdk_medialive.types.preferred_channel_pipeline.serialize_json(
                value["preferred_channel_pipeline"]
            )
        )
    if "program_number" in value:
        out["programNumber"] = value["program_number"]
    if "service_descriptor" in value:
        import aws_sdk_medialive.types.multiplex_program_service_descriptor

        out["serviceDescriptor"] = (
            aws_sdk_medialive.types.multiplex_program_service_descriptor.serialize_json(
                value["service_descriptor"]
            )
        )
    if "video_settings" in value:
        import aws_sdk_medialive.types.multiplex_video_settings

        out["videoSettings"] = (
            aws_sdk_medialive.types.multiplex_video_settings.serialize_json(
                value["video_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> MultiplexProgramSettings:
    out: MultiplexProgramSettings = {}  # type: ignore[typeddict-item]
    if "preferredChannelPipeline" in data:
        import aws_sdk_medialive.types.preferred_channel_pipeline

        out["preferred_channel_pipeline"] = (
            aws_sdk_medialive.types.preferred_channel_pipeline.deserialize_json(
                data["preferredChannelPipeline"]
            )
        )
    if "programNumber" in data:
        out["program_number"] = data["programNumber"]
    if "serviceDescriptor" in data:
        import aws_sdk_medialive.types.multiplex_program_service_descriptor

        out["service_descriptor"] = (
            aws_sdk_medialive.types.multiplex_program_service_descriptor.deserialize_json(
                data["serviceDescriptor"]
            )
        )
    if "videoSettings" in data:
        import aws_sdk_medialive.types.multiplex_video_settings

        out["video_settings"] = (
            aws_sdk_medialive.types.multiplex_video_settings.deserialize_json(
                data["videoSettings"]
            )
        )
    return out
