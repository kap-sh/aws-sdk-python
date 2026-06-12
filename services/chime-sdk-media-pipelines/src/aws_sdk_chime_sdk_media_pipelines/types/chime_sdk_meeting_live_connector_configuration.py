"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ChimeSdkMeetingLiveConnectorConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.arn
    import aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_mux_type
    import aws_sdk_chime_sdk_media_pipelines.types.source_configuration


class ChimeSdkMeetingLiveConnectorConfiguration(TypedDict):
    arn: "aws_sdk_chime_sdk_media_pipelines.types.arn.Arn"
    """<p>The configuration object's Chime SDK meeting ARN.</p>"""
    mux_type: "aws_sdk_chime_sdk_media_pipelines.types.live_connector_mux_type.LiveConnectorMuxType"
    """<p>The configuration object's multiplex type.</p>"""
    composited_video: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.CompositedVideoArtifactsConfiguration"
    ]
    """<p>The media pipeline's composited video.</p>"""
    source_configuration: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.source_configuration.SourceConfiguration"
    ]
    """<p>The source configuration settings of the media pipeline's configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ChimeSdkMeetingLiveConnectorConfiguration) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_mux_type

    out["MuxType"] = (
        aws_sdk_chime_sdk_media_pipelines.types.live_connector_mux_type.serialize_json(
            value["mux_type"]
        )
    )
    if "composited_video" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["CompositedVideo"] = (
            aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.serialize_json(
                value["composited_video"]
            )
        )
    if "source_configuration" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.source_configuration

        out["SourceConfiguration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.source_configuration.serialize_json(
                value["source_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ChimeSdkMeetingLiveConnectorConfiguration:
    out: ChimeSdkMeetingLiveConnectorConfiguration = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError(
            "ChimeSdkMeetingLiveConnectorConfiguration.arn required"
        )
    if "MuxType" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.live_connector_mux_type

        out["mux_type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.live_connector_mux_type.deserialize_json(
                data["MuxType"]
            )
        )
    else:
        raise DeserializationError(
            "ChimeSdkMeetingLiveConnectorConfiguration.mux_type required"
        )
    if "CompositedVideo" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration

        out["composited_video"] = (
            aws_sdk_chime_sdk_media_pipelines.types.composited_video_artifacts_configuration.deserialize_json(
                data["CompositedVideo"]
            )
        )
    if "SourceConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.source_configuration

        out["source_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.source_configuration.deserialize_json(
                data["SourceConfiguration"]
            )
        )
    return out
