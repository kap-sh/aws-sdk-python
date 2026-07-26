"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ScaleInPolicyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__integer


class ScaleInPolicyDescription(TypedDict, closed=True):
    cpu_utilization_percentage: "capo_kafkaconnect.types.__integer.__integer"
    """<p>Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScaleInPolicyDescription) -> dict:
    out: dict = {}
    out["cpuUtilizationPercentage"] = value.get("cpu_utilization_percentage", 0)
    return out


def deserialize_json(data: dict) -> ScaleInPolicyDescription:
    out: ScaleInPolicyDescription = {}  # type: ignore[typeddict-item]
    if "cpuUtilizationPercentage" in data:
        out["cpu_utilization_percentage"] = data["cpuUtilizationPercentage"]
    else:
        out["cpu_utilization_percentage"] = 0
    return out
