"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ScaleOutPolicy``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__integer_min1_max100


class ScaleOutPolicy(TypedDict):
    cpu_utilization_percentage: (
        "aws_sdk_kafkaconnect.types.__integer_min1_max100.__integerMin1Max100"
    )
    """<p>The CPU utilization percentage threshold at which you want connector scale out to be triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScaleOutPolicy) -> dict:
    out: dict = {}
    out["cpuUtilizationPercentage"] = value.get("cpu_utilization_percentage", 0)
    return out


def deserialize_json(data: dict) -> ScaleOutPolicy:
    out: ScaleOutPolicy = {}  # type: ignore[typeddict-item]
    if "cpuUtilizationPercentage" in data:
        out["cpu_utilization_percentage"] = data["cpuUtilizationPercentage"]
    else:
        out["cpu_utilization_percentage"] = 0
    return out
