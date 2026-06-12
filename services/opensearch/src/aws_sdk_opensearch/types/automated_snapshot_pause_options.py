"""Generated from Smithy shape ``com.amazonaws.opensearch#AutomatedSnapshotPauseOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.boolean
    import aws_sdk_opensearch.types.pause_state
    import aws_sdk_opensearch.types.timestamp


class AutomatedSnapshotPauseOptions(TypedDict):
    enabled: "aws_sdk_opensearch.types.boolean.Boolean"
    """<p>Whether automated snapshot pause is enabled for the domain.</p>"""
    start_time: NotRequired["aws_sdk_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp at which the automated snapshot pause begins.</p>"""
    end_time: NotRequired["aws_sdk_opensearch.types.timestamp.Timestamp"]
    """<p>The timestamp at which the automated snapshot pause ends.</p>"""
    state: NotRequired["aws_sdk_opensearch.types.pause_state.PauseState"]
    """<p>The current state of the automated snapshot pause. Valid values are <code>Active</code>, <code>Completed</code>, <code>Scheduled</code>, and <code>Disabled</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedSnapshotPauseOptions) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "start_time" in value:
        import aws_sdk_opensearch.types.timestamp

        out["StartTime"] = aws_sdk_opensearch.types.timestamp.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_opensearch.types.timestamp

        out["EndTime"] = aws_sdk_opensearch.types.timestamp.serialize_json(
            value["end_time"]
        )
    if "state" in value:
        import aws_sdk_opensearch.types.pause_state

        out["State"] = aws_sdk_opensearch.types.pause_state.serialize_json(
            value["state"]
        )
    return out


def deserialize_json(data: dict) -> AutomatedSnapshotPauseOptions:
    out: AutomatedSnapshotPauseOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError("AutomatedSnapshotPauseOptions.enabled required")
    if "StartTime" in data:
        import aws_sdk_opensearch.types.timestamp

        out["start_time"] = aws_sdk_opensearch.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    if "EndTime" in data:
        import aws_sdk_opensearch.types.timestamp

        out["end_time"] = aws_sdk_opensearch.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    if "State" in data:
        import aws_sdk_opensearch.types.pause_state

        out["state"] = aws_sdk_opensearch.types.pause_state.deserialize_json(
            data["State"]
        )
    return out
