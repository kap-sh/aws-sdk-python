"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#ScaleInPolicy``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__integer_min1_max100


class ScaleInPolicy(TypedDict):
    cpu_utilization_percentage: (
        "aws_sdk_kafkaconnect.types.__integer_min1_max100.__integerMin1Max100"
    )
    """<p>Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScaleInPolicy) -> dict:
    out: dict = {}
    out["cpuUtilizationPercentage"] = value.get("cpu_utilization_percentage", 0)
    return out


def deserialize_json(data: dict) -> ScaleInPolicy:
    out: ScaleInPolicy = {}  # type: ignore[typeddict-item]
    if "cpuUtilizationPercentage" in data:
        out["cpu_utilization_percentage"] = data["cpuUtilizationPercentage"]
    else:
        out["cpu_utilization_percentage"] = 0
    return out
