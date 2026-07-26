"""Generated from Smithy shape ``com.amazonaws.medialive#PipelineDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.channel_engine_version_response
    import capo_medialive.types.media_connect_router_output_connections


class PipelineDetail(TypedDict, closed=True):
    active_input_attachment_name: NotRequired["capo_medialive.types.__string.__string"]
    """The name of the active input attachment currently being ingested by this pipeline."""
    active_input_switch_action_name: NotRequired[
        "capo_medialive.types.__string.__string"
    ]
    """The name of the input switch schedule action that occurred most recently and that resulted in the switch to the current input attachment for this pipeline."""
    active_motion_graphics_action_name: NotRequired[
        "capo_medialive.types.__string.__string"
    ]
    """The name of the motion graphics activate action that occurred most recently and that resulted in the current graphics URI for this pipeline."""
    active_motion_graphics_uri: NotRequired["capo_medialive.types.__string.__string"]
    """The current URI being used for HTML5 motion graphics for this pipeline."""
    pipeline_id: NotRequired["capo_medialive.types.__string.__string"]
    """Pipeline ID"""
    channel_engine_version: NotRequired[
        "capo_medialive.types.channel_engine_version_response.ChannelEngineVersionResponse"
    ]
    """Current engine version of the encoder for this pipeline."""
    media_connect_router_output_connection_map: NotRequired[
        "capo_medialive.types.media_connect_router_output_connections.MediaConnectRouterOutputConnections"
    ]
    """A map of output names to the MediaConnect Router connection for this pipeline. Only present for channels with MediaConnect Router outputs."""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineDetail) -> dict:
    out: dict = {}
    if "active_input_attachment_name" in value:
        out["activeInputAttachmentName"] = value["active_input_attachment_name"]
    if "active_input_switch_action_name" in value:
        out["activeInputSwitchActionName"] = value["active_input_switch_action_name"]
    if "active_motion_graphics_action_name" in value:
        out["activeMotionGraphicsActionName"] = value[
            "active_motion_graphics_action_name"
        ]
    if "active_motion_graphics_uri" in value:
        out["activeMotionGraphicsUri"] = value["active_motion_graphics_uri"]
    if "pipeline_id" in value:
        out["pipelineId"] = value["pipeline_id"]
    if "channel_engine_version" in value:
        import capo_medialive.types.channel_engine_version_response

        out["channelEngineVersion"] = (
            capo_medialive.types.channel_engine_version_response.serialize_json(
                value["channel_engine_version"]
            )
        )
    if "media_connect_router_output_connection_map" in value:
        import capo_medialive.types.media_connect_router_output_connections

        out["mediaConnectRouterOutputConnectionMap"] = (
            capo_medialive.types.media_connect_router_output_connections.serialize_json(
                value["media_connect_router_output_connection_map"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipelineDetail:
    out: PipelineDetail = {}  # type: ignore[typeddict-item]
    if "activeInputAttachmentName" in data:
        out["active_input_attachment_name"] = data["activeInputAttachmentName"]
    if "activeInputSwitchActionName" in data:
        out["active_input_switch_action_name"] = data["activeInputSwitchActionName"]
    if "activeMotionGraphicsActionName" in data:
        out["active_motion_graphics_action_name"] = data[
            "activeMotionGraphicsActionName"
        ]
    if "activeMotionGraphicsUri" in data:
        out["active_motion_graphics_uri"] = data["activeMotionGraphicsUri"]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    if "channelEngineVersion" in data:
        import capo_medialive.types.channel_engine_version_response

        out["channel_engine_version"] = (
            capo_medialive.types.channel_engine_version_response.deserialize_json(
                data["channelEngineVersion"]
            )
        )
    if "mediaConnectRouterOutputConnectionMap" in data:
        import capo_medialive.types.media_connect_router_output_connections

        out["media_connect_router_output_connection_map"] = (
            capo_medialive.types.media_connect_router_output_connections.deserialize_json(
                data["mediaConnectRouterOutputConnectionMap"]
            )
        )
    return out
