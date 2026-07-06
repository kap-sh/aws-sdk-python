"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#RecordingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.composition_recording_hls_configuration
    import aws_sdk_ivs_realtime.types.recording_configuration_format


class RecordingConfiguration(TypedDict, closed=True):
    hls_configuration: NotRequired[
        "aws_sdk_ivs_realtime.types.composition_recording_hls_configuration.CompositionRecordingHlsConfiguration"
    ]
    """<p>An HLS configuration object to return information about how the recording will be configured.</p>"""
    format: NotRequired[
        "aws_sdk_ivs_realtime.types.recording_configuration_format.RecordingConfigurationFormat"
    ]
    """<p>The recording format for storing a recording in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RecordingConfiguration) -> dict:
    out: dict = {}
    if "hls_configuration" in value:
        import aws_sdk_ivs_realtime.types.composition_recording_hls_configuration

        out["hlsConfiguration"] = (
            aws_sdk_ivs_realtime.types.composition_recording_hls_configuration.serialize_json(
                value["hls_configuration"]
            )
        )
    if "format" in value:
        out["format"] = value["format"]
    return out


def deserialize_json(data: dict) -> RecordingConfiguration:
    out: RecordingConfiguration = {}  # type: ignore[typeddict-item]
    if "hlsConfiguration" in data:
        import aws_sdk_ivs_realtime.types.composition_recording_hls_configuration

        out["hls_configuration"] = (
            aws_sdk_ivs_realtime.types.composition_recording_hls_configuration.deserialize_json(
                data["hlsConfiguration"]
            )
        )
    if "format" in data:
        out["format"] = data["format"]
    return out
