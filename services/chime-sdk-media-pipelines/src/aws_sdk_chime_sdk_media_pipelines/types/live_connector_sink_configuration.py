"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSinkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_type


class LiveConnectorSinkConfiguration(TypedDict):
    sink_type: "aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_type.LiveConnectorSinkType"
    """<p>The sink configuration's sink type.</p>"""
    rtmp_configuration: "aws_sdk_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration.LiveConnectorRTMPConfiguration"
    """<p>The sink configuration's RTMP configuration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorSinkConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_type

    out["SinkType"] = (
        aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_type.serialize_json(
            value["sink_type"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration

    out["RTMPConfiguration"] = (
        aws_sdk_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration.serialize_json(
            value["rtmp_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> LiveConnectorSinkConfiguration:
    out: LiveConnectorSinkConfiguration = {}  # type: ignore[typeddict-item]
    if "SinkType" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_type

        out["sink_type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_type.deserialize_json(
                data["SinkType"]
            )
        )
    else:
        raise DeserializationError("LiveConnectorSinkConfiguration.sink_type required")
    if "RTMPConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration

        out["rtmp_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.live_connector_rtmp_configuration.deserialize_json(
                data["RTMPConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "LiveConnectorSinkConfiguration.rtmp_configuration required"
        )
    return out
