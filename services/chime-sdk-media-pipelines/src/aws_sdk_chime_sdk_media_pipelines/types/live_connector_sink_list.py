"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#LiveConnectorSinkList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_configuration

LiveConnectorSinkList: TypeAlias = list[
    "aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_configuration.LiveConnectorSinkConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: LiveConnectorSinkList) -> list:
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> LiveConnectorSinkList:
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_configuration

    out: LiveConnectorSinkList = []
    for item in data:
        out.append(
            aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_configuration.deserialize_json(
                item
            )
        )
    return out
