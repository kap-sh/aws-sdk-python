"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetCloudWatchLogsParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.json_path
    import capo_pipes.types.log_stream_name


class PipeTargetCloudWatchLogsParameters(TypedDict, closed=True):
    log_stream_name: NotRequired["capo_pipes.types.log_stream_name.LogStreamName"]
    """<p>The name of the log stream.</p>"""
    timestamp: NotRequired["capo_pipes.types.json_path.JsonPath"]
    """<p>The time the event occurred, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetCloudWatchLogsParameters) -> dict:
    out: dict = {}
    if "log_stream_name" in value:
        out["LogStreamName"] = value["log_stream_name"]
    if "timestamp" in value:
        out["Timestamp"] = value["timestamp"]
    return out


def deserialize_json(data: dict) -> PipeTargetCloudWatchLogsParameters:
    out: PipeTargetCloudWatchLogsParameters = {}  # type: ignore[typeddict-item]
    if "LogStreamName" in data:
        out["log_stream_name"] = data["LogStreamName"]
    if "Timestamp" in data:
        out["timestamp"] = data["Timestamp"]
    return out
