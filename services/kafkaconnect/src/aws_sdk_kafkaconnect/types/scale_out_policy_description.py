"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ScaleOutPolicyDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__integer


class ScaleOutPolicyDescription(TypedDict, closed=True):
    cpu_utilization_percentage: "aws_sdk_kafkaconnect.types.__integer.__integer"
    """<p>The CPU utilization percentage threshold at which you want connector scale out to be triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScaleOutPolicyDescription) -> dict:
    out: dict = {}
    out["cpuUtilizationPercentage"] = value.get("cpu_utilization_percentage", 0)
    return out


def deserialize_json(data: dict) -> ScaleOutPolicyDescription:
    out: ScaleOutPolicyDescription = {}  # type: ignore[typeddict-item]
    if "cpuUtilizationPercentage" in data:
        out["cpu_utilization_percentage"] = data["cpuUtilizationPercentage"]
    else:
        out["cpu_utilization_percentage"] = 0
    return out
