"""Generated from Smithy shape ``com.amazonaws.emrserverless#SchedulerConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class SchedulerConfiguration(TypedDict, closed=True):
    queue_timeout_minutes: NotRequired["int"]
    """<p>The maximum duration in minutes for the job in QUEUED state. If scheduler configuration is enabled on your application, the default value is 360 minutes (6 hours). The valid range is from 15 to 720.</p>"""
    max_concurrent_runs: NotRequired["int"]
    """<p>The maximum concurrent job runs on this application. If scheduler configuration is enabled on your application, the default value is 15. The valid range is 1 to 1000.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SchedulerConfiguration) -> dict:
    out: dict = {}
    if "queue_timeout_minutes" in value:
        out["queueTimeoutMinutes"] = value["queue_timeout_minutes"]
    if "max_concurrent_runs" in value:
        out["maxConcurrentRuns"] = value["max_concurrent_runs"]
    return out


def deserialize_json(data: dict) -> SchedulerConfiguration:
    out: SchedulerConfiguration = {}  # type: ignore[typeddict-item]
    if "queueTimeoutMinutes" in data:
        out["queue_timeout_minutes"] = data["queueTimeoutMinutes"]
    if "maxConcurrentRuns" in data:
        out["max_concurrent_runs"] = data["maxConcurrentRuns"]
    return out
