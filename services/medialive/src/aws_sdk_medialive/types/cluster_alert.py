"""Generated from Smithy shape ``com.amazonaws.medialive#ClusterAlert``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string
    import aws_sdk_medialive.types.__timestamp_iso8601
    import aws_sdk_medialive.types.cluster_alert_state


class ClusterAlert(TypedDict):
    alert_type: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The type of the alert"""
    channel_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the channel this alert is associated with"""
    cleared_timestamp: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """The time when the alert was cleared"""
    id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The further subtype of this alert"""
    message: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The user facing alert message which can have more context"""
    node_id: NotRequired["aws_sdk_medialive.types.__string.__string"]
    """The ID of the node this alert is associated with"""
    set_timestamp: NotRequired[
        "aws_sdk_medialive.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """The time when the alert was set"""
    state: NotRequired["aws_sdk_medialive.types.cluster_alert_state.ClusterAlertState"]
    """The state of the alert"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterAlert) -> dict:
    out: dict = {}
    if "alert_type" in value:
        out["alertType"] = value["alert_type"]
    if "channel_id" in value:
        out["channelId"] = value["channel_id"]
    if "cleared_timestamp" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["clearedTimestamp"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
                value["cleared_timestamp"]
            )
        )
    if "id" in value:
        out["id"] = value["id"]
    if "message" in value:
        out["message"] = value["message"]
    if "node_id" in value:
        out["nodeId"] = value["node_id"]
    if "set_timestamp" in value:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["setTimestamp"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.serialize_json(
                value["set_timestamp"]
            )
        )
    if "state" in value:
        import aws_sdk_medialive.types.cluster_alert_state

        out["state"] = aws_sdk_medialive.types.cluster_alert_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> ClusterAlert:
    out: ClusterAlert = {}  # type: ignore[typeddict-item]
    if "alertType" in data:
        out["alert_type"] = data["alertType"]
    if "channelId" in data:
        out["channel_id"] = data["channelId"]
    if "clearedTimestamp" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["cleared_timestamp"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["clearedTimestamp"]
            )
        )
    if "id" in data:
        out["id"] = data["id"]
    if "message" in data:
        out["message"] = data["message"]
    if "nodeId" in data:
        out["node_id"] = data["nodeId"]
    if "setTimestamp" in data:
        import aws_sdk_medialive.types.__timestamp_iso8601

        out["set_timestamp"] = (
            aws_sdk_medialive.types.__timestamp_iso8601.deserialize_json(
                data["setTimestamp"]
            )
        )
    if "state" in data:
        import aws_sdk_medialive.types.cluster_alert_state

        out["state"] = aws_sdk_medialive.types.cluster_alert_state.deserialize_json(
            data["state"]
        )
    return out
