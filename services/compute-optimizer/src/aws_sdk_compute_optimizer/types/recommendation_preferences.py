"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#RecommendationPreferences``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.cpu_vendor_architectures


class RecommendationPreferences(TypedDict):
    cpu_vendor_architectures: NotRequired[
        "aws_sdk_compute_optimizer.types.cpu_vendor_architectures.CpuVendorArchitectures"
    ]
    """<p>Specifies the CPU vendor and architecture for Amazon EC2 instance and Auto Scaling group recommendations.</p> <p>For example, when you specify <code>AWS_ARM64</code> with:</p> <ul> <li> <p>A <a>GetEC2InstanceRecommendations</a> or <a>GetAutoScalingGroupRecommendations</a> request, Compute Optimizer returns recommendations that consist of Graviton instance types only.</p> </li> <li> <p>A <a>GetEC2RecommendationProjectedMetrics</a> request, Compute Optimizer returns projected utilization metrics for Graviton instance type recommendations only.</p> </li> <li> <p>A <a>ExportEC2InstanceRecommendations</a> or <a>ExportAutoScalingGroupRecommendations</a> request, Compute Optimizer exports recommendations that consist of Graviton instance types only.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendationPreferences) -> dict:
    out: dict = {}
    if "cpu_vendor_architectures" in value:
        import aws_sdk_compute_optimizer.types.cpu_vendor_architectures

        out["cpuVendorArchitectures"] = (
            aws_sdk_compute_optimizer.types.cpu_vendor_architectures.serialize_aws_json_1_0(
                value["cpu_vendor_architectures"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RecommendationPreferences:
    out: RecommendationPreferences = {}  # type: ignore[typeddict-item]
    if "cpuVendorArchitectures" in data:
        import aws_sdk_compute_optimizer.types.cpu_vendor_architectures

        out["cpu_vendor_architectures"] = (
            aws_sdk_compute_optimizer.types.cpu_vendor_architectures.deserialize_aws_json_1_0(
                data["cpuVendorArchitectures"]
            )
        )
    return out
