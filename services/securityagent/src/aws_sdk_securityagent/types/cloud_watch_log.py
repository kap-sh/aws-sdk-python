"""Generated from Smithy shape ``com.amazonaws.securityagent#CloudWatchLog``."""

from typing_extensions import NotRequired, TypedDict


class CloudWatchLog(TypedDict, closed=True):
    log_group: NotRequired["str"]
    """<p>The name of the CloudWatch log group.</p>"""
    log_stream: NotRequired["str"]
    """<p>The name of the CloudWatch log stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CloudWatchLog) -> dict:
    out: dict = {}
    if "log_group" in value:
        out["logGroup"] = value["log_group"]
    if "log_stream" in value:
        out["logStream"] = value["log_stream"]
    return out


def deserialize_json(data: dict) -> CloudWatchLog:
    out: CloudWatchLog = {}  # type: ignore[typeddict-item]
    if "logGroup" in data:
        out["log_group"] = data["logGroup"]
    if "logStream" in data:
        out["log_stream"] = data["logStream"]
    return out
