"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaLiveConnectorPipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.client_request_token
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_list
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_source_list
    import aws_sdk_chime_sdk_media_pipelines.types.tag_list


class CreateMediaLiveConnectorPipelineRequest(TypedDict, closed=True):
    sources: "aws_sdk_chime_sdk_media_pipelines.types.live_connector_source_list.LiveConnectorSourceList"
    """<p>The media live connector pipeline's data sources.</p>"""
    sinks: "aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_list.LiveConnectorSinkList"
    """<p>The media live connector pipeline's data sinks.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The token assigned to the client making the request.</p>"""
    tags: NotRequired["aws_sdk_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tags associated with the media live connector pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaLiveConnectorPipelineRequest) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_source_list

    out["Sources"] = (
        aws_sdk_chime_sdk_media_pipelines.types.live_connector_source_list.serialize_json(
            value["sources"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_list

    out["Sinks"] = (
        aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_list.serialize_json(
            value["sinks"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import aws_sdk_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = aws_sdk_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMediaLiveConnectorPipelineRequest:
    out: CreateMediaLiveConnectorPipelineRequest = {}  # type: ignore[typeddict-item]
    if "Sources" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.live_connector_source_list

        out["sources"] = (
            aws_sdk_chime_sdk_media_pipelines.types.live_connector_source_list.deserialize_json(
                data["Sources"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMediaLiveConnectorPipelineRequest.sources required"
        )
    if "Sinks" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_list

        out["sinks"] = (
            aws_sdk_chime_sdk_media_pipelines.types.live_connector_sink_list.deserialize_json(
                data["Sinks"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMediaLiveConnectorPipelineRequest.sinks required"
        )
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = aws_sdk_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
