"""Generated from Smithy shape ``com.amazonaws.ivs#IngestConfigurations``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ivs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs.types.audio_configuration_list
    import aws_sdk_ivs.types.video_configuration_list


class IngestConfigurations(TypedDict):
    video_configurations: (
        "aws_sdk_ivs.types.video_configuration_list.VideoConfigurationList"
    )
    """<p>Encoder settings for video</p>"""
    audio_configurations: (
        "aws_sdk_ivs.types.audio_configuration_list.AudioConfigurationList"
    )
    """<p>Encoder settings for audio.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfigurations) -> dict:
    out: dict = {}
    import aws_sdk_ivs.types.video_configuration_list

    out["videoConfigurations"] = (
        aws_sdk_ivs.types.video_configuration_list.serialize_json(
            value["video_configurations"]
        )
    )
    import aws_sdk_ivs.types.audio_configuration_list

    out["audioConfigurations"] = (
        aws_sdk_ivs.types.audio_configuration_list.serialize_json(
            value["audio_configurations"]
        )
    )
    return out


def deserialize_json(data: dict) -> IngestConfigurations:
    out: IngestConfigurations = {}  # type: ignore[typeddict-item]
    if "videoConfigurations" in data:
        import aws_sdk_ivs.types.video_configuration_list

        out["video_configurations"] = (
            aws_sdk_ivs.types.video_configuration_list.deserialize_json(
                data["videoConfigurations"]
            )
        )
    else:
        raise DeserializationError("IngestConfigurations.video_configurations required")
    if "audioConfigurations" in data:
        import aws_sdk_ivs.types.audio_configuration_list

        out["audio_configurations"] = (
            aws_sdk_ivs.types.audio_configuration_list.deserialize_json(
                data["audioConfigurations"]
            )
        )
    else:
        raise DeserializationError("IngestConfigurations.audio_configurations required")
    return out
