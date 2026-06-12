"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#PipConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.attribute_key
    import aws_sdk_ivs_realtime.types.grid_gap
    import aws_sdk_ivs_realtime.types.omit_stopped_video
    import aws_sdk_ivs_realtime.types.pip_behavior
    import aws_sdk_ivs_realtime.types.pip_height
    import aws_sdk_ivs_realtime.types.pip_offset
    import aws_sdk_ivs_realtime.types.pip_position
    import aws_sdk_ivs_realtime.types.pip_width
    import aws_sdk_ivs_realtime.types.video_fill_mode


class PipConfiguration(TypedDict):
    featured_participant_attribute: NotRequired[
        "aws_sdk_ivs_realtime.types.attribute_key.AttributeKey"
    ]
    """<p>This attribute name identifies the featured slot. A participant with this attribute set to <code>\"true\"</code> (as a string value) in <a>ParticipantTokenConfiguration</a> is placed in the featured slot. Default: <code>\"\"</code> (no featured participant).</p>"""
    omit_stopped_video: "aws_sdk_ivs_realtime.types.omit_stopped_video.OmitStoppedVideo"
    """<p>Determines whether to omit participants with stopped video in the composition. Default: <code>false</code>.</p>"""
    video_fill_mode: NotRequired[
        "aws_sdk_ivs_realtime.types.video_fill_mode.VideoFillMode"
    ]
    """<p>Defines how video content fits within the participant tile: <code>FILL</code> (stretched), <code>COVER</code> (cropped), or <code>CONTAIN</code> (letterboxed). Default: <code>COVER</code>.</p>"""
    grid_gap: "aws_sdk_ivs_realtime.types.grid_gap.GridGap"
    """<p>Specifies the spacing between participant tiles in pixels. Default: <code>0</code>.</p>"""
    pip_participant_attribute: NotRequired[
        "aws_sdk_ivs_realtime.types.attribute_key.AttributeKey"
    ]
    """<p>Specifies the participant for the PiP window. A participant with this attribute set to <code>\"true\"</code> (as a string value) in <a>ParticipantTokenConfiguration</a> is placed in the PiP slot. Default: <code>\"\"</code> (no PiP participant).</p>"""
    pip_behavior: NotRequired["aws_sdk_ivs_realtime.types.pip_behavior.PipBehavior"]
    """<p>Defines PiP behavior when all participants have left: <code>STATIC</code> (maintains original position/size) or <code>DYNAMIC</code> (expands to full composition). Default: <code>STATIC</code>.</p>"""
    pip_offset: "aws_sdk_ivs_realtime.types.pip_offset.PipOffset"
    """<p>Sets the PiP window’s offset position in pixels from the closest edges determined by <code>PipPosition</code>. Default: <code>0</code>.</p>"""
    pip_position: NotRequired["aws_sdk_ivs_realtime.types.pip_position.PipPosition"]
    """<p>Determines the corner position of the PiP window. Default: <code>BOTTOM_RIGHT</code>.</p>"""
    pip_width: NotRequired["aws_sdk_ivs_realtime.types.pip_width.PipWidth"]
    """<p>Specifies the width of the PiP window in pixels. When this is not set explicitly, <code>pipWidth</code>’s value will be based on the size of the composition and the aspect ratio of the participant’s video.</p>"""
    pip_height: NotRequired["aws_sdk_ivs_realtime.types.pip_height.PipHeight"]
    """<p>Specifies the height of the PiP window in pixels. When this is not set explicitly, <code>pipHeight</code>’s value will be based on the size of the composition and the aspect ratio of the participant’s video.</p>"""
    participant_order_attribute: NotRequired[
        "aws_sdk_ivs_realtime.types.attribute_key.AttributeKey"
    ]
    """<p>Attribute name in <a>ParticipantTokenConfiguration</a> identifying the participant ordering key. Participants with <code>participantOrderAttribute</code> set to <code>\"\"</code> or not specified are ordered based on their arrival time into the stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipConfiguration) -> dict:
    out: dict = {}
    if "featured_participant_attribute" in value:
        out["featuredParticipantAttribute"] = value["featured_participant_attribute"]
    out["omitStoppedVideo"] = value.get("omit_stopped_video", False)
    if "video_fill_mode" in value:
        import aws_sdk_ivs_realtime.types.video_fill_mode

        out["videoFillMode"] = (
            aws_sdk_ivs_realtime.types.video_fill_mode.serialize_json(
                value["video_fill_mode"]
            )
        )
    out["gridGap"] = value.get("grid_gap", 0)
    if "pip_participant_attribute" in value:
        out["pipParticipantAttribute"] = value["pip_participant_attribute"]
    if "pip_behavior" in value:
        import aws_sdk_ivs_realtime.types.pip_behavior

        out["pipBehavior"] = aws_sdk_ivs_realtime.types.pip_behavior.serialize_json(
            value["pip_behavior"]
        )
    out["pipOffset"] = value.get("pip_offset", 0)
    if "pip_position" in value:
        import aws_sdk_ivs_realtime.types.pip_position

        out["pipPosition"] = aws_sdk_ivs_realtime.types.pip_position.serialize_json(
            value["pip_position"]
        )
    if "pip_width" in value:
        out["pipWidth"] = value["pip_width"]
    if "pip_height" in value:
        out["pipHeight"] = value["pip_height"]
    if "participant_order_attribute" in value:
        out["participantOrderAttribute"] = value["participant_order_attribute"]
    return out


def deserialize_json(data: dict) -> PipConfiguration:
    out: PipConfiguration = {}  # type: ignore[typeddict-item]
    if "featuredParticipantAttribute" in data:
        out["featured_participant_attribute"] = data["featuredParticipantAttribute"]
    if "omitStoppedVideo" in data:
        out["omit_stopped_video"] = data["omitStoppedVideo"]
    else:
        out["omit_stopped_video"] = False
    if "videoFillMode" in data:
        import aws_sdk_ivs_realtime.types.video_fill_mode

        out["video_fill_mode"] = (
            aws_sdk_ivs_realtime.types.video_fill_mode.deserialize_json(
                data["videoFillMode"]
            )
        )
    if "gridGap" in data:
        out["grid_gap"] = data["gridGap"]
    else:
        out["grid_gap"] = 0
    if "pipParticipantAttribute" in data:
        out["pip_participant_attribute"] = data["pipParticipantAttribute"]
    if "pipBehavior" in data:
        import aws_sdk_ivs_realtime.types.pip_behavior

        out["pip_behavior"] = aws_sdk_ivs_realtime.types.pip_behavior.deserialize_json(
            data["pipBehavior"]
        )
    if "pipOffset" in data:
        out["pip_offset"] = data["pipOffset"]
    else:
        out["pip_offset"] = 0
    if "pipPosition" in data:
        import aws_sdk_ivs_realtime.types.pip_position

        out["pip_position"] = aws_sdk_ivs_realtime.types.pip_position.deserialize_json(
            data["pipPosition"]
        )
    if "pipWidth" in data:
        out["pip_width"] = data["pipWidth"]
    if "pipHeight" in data:
        out["pip_height"] = data["pipHeight"]
    if "participantOrderAttribute" in data:
        out["participant_order_attribute"] = data["participantOrderAttribute"]
    return out
