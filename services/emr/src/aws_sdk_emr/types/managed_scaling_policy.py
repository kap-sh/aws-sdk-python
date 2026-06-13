"""Generated from Smithy shape ``com.amazonaws.emr#ManagedScalingPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.compute_limits
    import aws_sdk_emr.types.scaling_strategy
    import aws_sdk_emr.types.utilization_performance_index_integer


class ManagedScalingPolicy(TypedDict):
    compute_limits: NotRequired["aws_sdk_emr.types.compute_limits.ComputeLimits"]
    """<p>The Amazon EC2 unit limits for a managed scaling policy. The managed scaling activity of a cluster is not allowed to go above or below these limits. The limit only applies to the core and task nodes. The master node cannot be scaled after initial configuration.</p>"""
    utilization_performance_index: NotRequired[
        "aws_sdk_emr.types.utilization_performance_index_integer.UtilizationPerformanceIndexInteger"
    ]
    """<p>An integer value that represents an advanced scaling strategy. Setting a higher value optimizes for performance. Setting a lower value optimizes for resource conservation. Setting the value to 50 balances performance and resource conservation. Possible values are 1, 25, 50, 75, and 100.</p>"""
    scaling_strategy: NotRequired["aws_sdk_emr.types.scaling_strategy.ScalingStrategy"]
    """<p>Determines whether a custom scaling utilization performance index can be set. Possible values include <i>ADVANCED</i> or <i>DEFAULT</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ManagedScalingPolicy) -> dict:
    out: dict = {}
    if "compute_limits" in value:
        import aws_sdk_emr.types.compute_limits

        out["ComputeLimits"] = aws_sdk_emr.types.compute_limits.serialize_aws_json_1_1(
            value["compute_limits"]
        )
    if "utilization_performance_index" in value:
        out["UtilizationPerformanceIndex"] = value["utilization_performance_index"]
    if "scaling_strategy" in value:
        import aws_sdk_emr.types.scaling_strategy

        out["ScalingStrategy"] = (
            aws_sdk_emr.types.scaling_strategy.serialize_aws_json_1_1(
                value["scaling_strategy"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ManagedScalingPolicy:
    out: ManagedScalingPolicy = {}  # type: ignore[typeddict-item]
    if "ComputeLimits" in data:
        import aws_sdk_emr.types.compute_limits

        out["compute_limits"] = (
            aws_sdk_emr.types.compute_limits.deserialize_aws_json_1_1(
                data["ComputeLimits"]
            )
        )
    if "UtilizationPerformanceIndex" in data:
        out["utilization_performance_index"] = data["UtilizationPerformanceIndex"]
    if "ScalingStrategy" in data:
        import aws_sdk_emr.types.scaling_strategy

        out["scaling_strategy"] = (
            aws_sdk_emr.types.scaling_strategy.deserialize_aws_json_1_1(
                data["ScalingStrategy"]
            )
        )
    return out
