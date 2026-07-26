"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#CreateMediaStreamPipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.client_request_token
    import capo_chime_sdk_media_pipelines.types.media_stream_sink_list
    import capo_chime_sdk_media_pipelines.types.media_stream_source_list
    import capo_chime_sdk_media_pipelines.types.tag_list


class CreateMediaStreamPipelineRequest(TypedDict, closed=True):
    sources: "capo_chime_sdk_media_pipelines.types.media_stream_source_list.MediaStreamSourceList"
    """<p>The data sources for the media pipeline.</p>"""
    sinks: "capo_chime_sdk_media_pipelines.types.media_stream_sink_list.MediaStreamSinkList"
    """<p>The data sink for the media pipeline.</p>"""
    client_request_token: NotRequired[
        "capo_chime_sdk_media_pipelines.types.client_request_token.ClientRequestToken"
    ]
    """<p>The token assigned to the client making the request.</p>"""
    tags: NotRequired["capo_chime_sdk_media_pipelines.types.tag_list.TagList"]
    """<p>The tags assigned to the media pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMediaStreamPipelineRequest) -> dict:
    out: dict = {}
    import capo_chime_sdk_media_pipelines.types.media_stream_source_list

    out["Sources"] = (
        capo_chime_sdk_media_pipelines.types.media_stream_source_list.serialize_json(
            value["sources"]
        )
    )
    import capo_chime_sdk_media_pipelines.types.media_stream_sink_list

    out["Sinks"] = (
        capo_chime_sdk_media_pipelines.types.media_stream_sink_list.serialize_json(
            value["sinks"]
        )
    )
    if "client_request_token" in value:
        out["ClientRequestToken"] = value["client_request_token"]
    if "tags" in value:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["Tags"] = capo_chime_sdk_media_pipelines.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateMediaStreamPipelineRequest:
    out: CreateMediaStreamPipelineRequest = {}  # type: ignore[typeddict-item]
    if "Sources" in data:
        import capo_chime_sdk_media_pipelines.types.media_stream_source_list

        out["sources"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_source_list.deserialize_json(
                data["Sources"]
            )
        )
    else:
        raise DeserializationError("CreateMediaStreamPipelineRequest.sources required")
    if "Sinks" in data:
        import capo_chime_sdk_media_pipelines.types.media_stream_sink_list

        out["sinks"] = (
            capo_chime_sdk_media_pipelines.types.media_stream_sink_list.deserialize_json(
                data["Sinks"]
            )
        )
    else:
        raise DeserializationError("CreateMediaStreamPipelineRequest.sinks required")
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    if "Tags" in data:
        import capo_chime_sdk_media_pipelines.types.tag_list

        out["tags"] = capo_chime_sdk_media_pipelines.types.tag_list.deserialize_json(
            data["Tags"]
        )
    return out
