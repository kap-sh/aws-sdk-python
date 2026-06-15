"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#Stage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ivs_realtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.auto_participant_recording_configuration
    import aws_sdk_ivs_realtime.types.stage_arn
    import aws_sdk_ivs_realtime.types.stage_endpoints
    import aws_sdk_ivs_realtime.types.stage_name
    import aws_sdk_ivs_realtime.types.stage_session_id
    import aws_sdk_ivs_realtime.types.tags


class Stage(TypedDict):
    arn: "aws_sdk_ivs_realtime.types.stage_arn.StageArn"
    """<p>Stage ARN.</p>"""
    name: NotRequired["aws_sdk_ivs_realtime.types.stage_name.StageName"]
    """<p>Stage name.</p>"""
    active_session_id: NotRequired[
        "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    ]
    """<p>ID of the active session within the stage.</p>"""
    tags: NotRequired["aws_sdk_ivs_realtime.types.tags.Tags"]
    r"""<p>Tags attached to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href=\"https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html\">Best practices and strategies</a> in <i>Tagging AWS Resources and Tag Editor</i> for details, including restrictions that apply to tags and \"Tag naming limits and requirements\"; Amazon IVS has no constraints on tags beyond what is documented there.</p>"""
    auto_participant_recording_configuration: NotRequired[
        "aws_sdk_ivs_realtime.types.auto_participant_recording_configuration.AutoParticipantRecordingConfiguration"
    ]
    """<p>Configuration object for individual participant recording, attached to the stage.</p>"""
    endpoints: NotRequired["aws_sdk_ivs_realtime.types.stage_endpoints.StageEndpoints"]
    """<p>Summary information about various endpoints for a stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Stage) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "active_session_id" in value:
        out["activeSessionId"] = value["active_session_id"]
    if "tags" in value:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.serialize_json(value["tags"])
    if "auto_participant_recording_configuration" in value:
        import aws_sdk_ivs_realtime.types.auto_participant_recording_configuration

        out["autoParticipantRecordingConfiguration"] = (
            aws_sdk_ivs_realtime.types.auto_participant_recording_configuration.serialize_json(
                value["auto_participant_recording_configuration"]
            )
        )
    if "endpoints" in value:
        import aws_sdk_ivs_realtime.types.stage_endpoints

        out["endpoints"] = aws_sdk_ivs_realtime.types.stage_endpoints.serialize_json(
            value["endpoints"]
        )
    return out


def deserialize_json(data: dict) -> Stage:
    out: Stage = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Stage.arn required")
    if "name" in data:
        out["name"] = data["name"]
    if "activeSessionId" in data:
        out["active_session_id"] = data["activeSessionId"]
    if "tags" in data:
        import aws_sdk_ivs_realtime.types.tags

        out["tags"] = aws_sdk_ivs_realtime.types.tags.deserialize_json(data["tags"])
    if "autoParticipantRecordingConfiguration" in data:
        import aws_sdk_ivs_realtime.types.auto_participant_recording_configuration

        out["auto_participant_recording_configuration"] = (
            aws_sdk_ivs_realtime.types.auto_participant_recording_configuration.deserialize_json(
                data["autoParticipantRecordingConfiguration"]
            )
        )
    if "endpoints" in data:
        import aws_sdk_ivs_realtime.types.stage_endpoints

        out["endpoints"] = aws_sdk_ivs_realtime.types.stage_endpoints.deserialize_json(
            data["endpoints"]
        )
    return out
