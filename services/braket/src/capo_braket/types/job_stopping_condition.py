"""Generated from Smithy shape ``com.amazonaws.braket#JobStoppingCondition``."""

from typing_extensions import NotRequired, TypedDict


class JobStoppingCondition(TypedDict, closed=True):
    max_runtime_in_seconds: NotRequired["int"]
    """<p>The maximum length of time, in seconds, that an Amazon Braket hybrid job can run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobStoppingCondition) -> dict:
    out: dict = {}
    if "max_runtime_in_seconds" in value:
        out["maxRuntimeInSeconds"] = value["max_runtime_in_seconds"]
    return out


def deserialize_json(data: dict) -> JobStoppingCondition:
    out: JobStoppingCondition = {}  # type: ignore[typeddict-item]
    if "maxRuntimeInSeconds" in data:
        out["max_runtime_in_seconds"] = data["maxRuntimeInSeconds"]
    return out
