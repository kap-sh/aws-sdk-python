"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StoppingCondition``."""

from typing_extensions import TypedDict


class StoppingCondition(TypedDict, closed=True):
    max_runtime_in_seconds: "int"
    """<p>The maximum amount of time, in seconds, that model training can run before it is terminated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StoppingCondition) -> dict:
    out: dict = {}
    out["maxRuntimeInSeconds"] = value.get("max_runtime_in_seconds", 86400)
    return out


def deserialize_json(data: dict) -> StoppingCondition:
    out: StoppingCondition = {}  # type: ignore[typeddict-item]
    if "maxRuntimeInSeconds" in data:
        out["max_runtime_in_seconds"] = data["maxRuntimeInSeconds"]
    else:
        out["max_runtime_in_seconds"] = 86400
    return out
