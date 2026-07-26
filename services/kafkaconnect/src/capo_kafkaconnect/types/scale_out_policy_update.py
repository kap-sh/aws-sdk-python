"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ScaleOutPolicyUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kafkaconnect.types.__integer_min1_max100


class ScaleOutPolicyUpdate(TypedDict, closed=True):
    cpu_utilization_percentage: (
        "capo_kafkaconnect.types.__integer_min1_max100.__integerMin1Max100"
    )
    """<p>The target CPU utilization percentage threshold at which you want connector scale out to be triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScaleOutPolicyUpdate) -> dict:
    out: dict = {}
    out["cpuUtilizationPercentage"] = value.get("cpu_utilization_percentage", 0)
    return out


def deserialize_json(data: dict) -> ScaleOutPolicyUpdate:
    out: ScaleOutPolicyUpdate = {}  # type: ignore[typeddict-item]
    if "cpuUtilizationPercentage" in data:
        out["cpu_utilization_percentage"] = data["cpuUtilizationPercentage"]
    else:
        out["cpu_utilization_percentage"] = 0
    return out
