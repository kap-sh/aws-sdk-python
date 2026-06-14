"""Generated from Smithy shape ``com.amazonaws.datazone#TimeoutConfig``."""

from typing import TypedDict

from typing_extensions import NotRequired


class TimeoutConfig(TypedDict):
    run_timeout_in_minutes: NotRequired["int"]
    """<p>The timeout for the notebook run, in minutes. The minimum value is 60 minutes (1 hour), the maximum value is 1440 minutes (24 hours), and the default value is 720 minutes (12 hours).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TimeoutConfig) -> dict:
    out: dict = {}
    if "run_timeout_in_minutes" in value:
        out["runTimeoutInMinutes"] = value["run_timeout_in_minutes"]
    return out


def deserialize_json(data: dict) -> TimeoutConfig:
    out: TimeoutConfig = {}  # type: ignore[typeddict-item]
    if "runTimeoutInMinutes" in data:
        out["run_timeout_in_minutes"] = data["runTimeoutInMinutes"]
    return out
