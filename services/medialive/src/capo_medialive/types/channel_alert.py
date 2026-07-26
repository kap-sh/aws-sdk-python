"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelAlert``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.__timestamp_iso8601
    import capo_medialive.types.channel_alert_state


class ChannelAlert(TypedDict, closed=True):
    alert_type: NotRequired["capo_medialive.types.__string.__string"]
    """The type of the alert"""
    cleared_timestamp: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """The time when the alert was cleared"""
    id: NotRequired["capo_medialive.types.__string.__string"]
    """The unique ID for this alert instance"""
    message: NotRequired["capo_medialive.types.__string.__string"]
    """The user facing alert message which can have more context"""
    pipeline_id: NotRequired["capo_medialive.types.__string.__string"]
    """The ID of the pipeline this alert is associated with"""
    set_timestamp: NotRequired[
        "capo_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """The time when the alert was set"""
    state: NotRequired["capo_medialive.types.channel_alert_state.ChannelAlertState"]
    """The state of the alert"""


# --- restJson1 ser/de ---
def serialize_json(value: ChannelAlert) -> dict:
    out: dict = {}
    if "alert_type" in value:
        out["alertType"] = value["alert_type"]
    if "cleared_timestamp" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["clearedTimestamp"] = (
            capo_medialive.types.__timestamp_iso8601.serialize_json(
                value["cleared_timestamp"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "message" in value:
        out["message"] = value["message"]
    if "pipeline_id" in value:
        out["pipelineId"] = value["pipeline_id"]
    if "set_timestamp" in value:
        import capo_medialive.types.__timestamp_iso8601

        out["setTimestamp"] = capo_medialive.types.__timestamp_iso8601.serialize_json(
            value["set_timestamp"]
        )
    if "state" in value:
        import capo_medialive.types.channel_alert_state

        out["state"] = capo_medialive.types.channel_alert_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ChannelAlert:
    out: ChannelAlert = {}  # type: ignore[typeddict-item]
    if "alertType" in data:
        out["alert_type"] = data["alertType"]
    if "clearedTimestamp" in data:
        import capo_medialive.types.__timestamp_iso8601

        out["cleared_timestamp"] = (
            capo_medialive.types.__timestamp_iso8601.deserialize_json(
                data["clearedTimestamp"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "message" in data:
        out["message"] = data["message"]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    if "setTimestamp" in data:
        import capo_medialive.types.__timestamp_iso8601

        out["set_timestamp"] = (
            capo_medialive.types.__timestamp_iso8601.deserialize_json(
                data["setTimestamp"]
            )
        )
    if "state" in data:
        import capo_medialive.types.channel_alert_state

        out["state"] = capo_medialive.types.channel_alert_state.deserialize_json(
            data["state"]
        )
    return out
