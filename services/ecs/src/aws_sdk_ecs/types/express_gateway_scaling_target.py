"""Generated from Smithy shape ``com.amazonaws.ecs#ExpressGatewayScalingTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.boxed_integer
    import aws_sdk_ecs.types.express_gateway_service_scaling_metric


class ExpressGatewayScalingTarget(TypedDict):
    min_task_count: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The minimum number of tasks to run in the Express service.</p>"""
    max_task_count: NotRequired["aws_sdk_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of tasks to run in the Express service.</p>"""
    auto_scaling_metric: NotRequired[
        "aws_sdk_ecs.types.express_gateway_service_scaling_metric.ExpressGatewayServiceScalingMetric"
    ]
    """<p>The metric used for auto-scaling decisions. The default metric used for an Express service is <code>CPUUtilization</code>.</p>"""
    auto_scaling_target_value: NotRequired[
        "aws_sdk_ecs.types.boxed_integer.BoxedInteger"
    ]
    """<p>The target value for the auto-scaling metric. The default value for an Express service is 60.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpressGatewayScalingTarget) -> dict:
    out: dict = {}
    if "min_task_count" in value:
        out["minTaskCount"] = value["min_task_count"]
    if "max_task_count" in value:
        out["maxTaskCount"] = value["max_task_count"]
    if "auto_scaling_metric" in value:
        import aws_sdk_ecs.types.express_gateway_service_scaling_metric

        out["autoScalingMetric"] = (
            aws_sdk_ecs.types.express_gateway_service_scaling_metric.serialize_aws_json_1_1(
                value["auto_scaling_metric"]
            )
        )
    if "auto_scaling_target_value" in value:
        out["autoScalingTargetValue"] = value["auto_scaling_target_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpressGatewayScalingTarget:
    out: ExpressGatewayScalingTarget = {}  # type: ignore[typeddict-item]
    if "minTaskCount" in data:
        out["min_task_count"] = data["minTaskCount"]
    if "maxTaskCount" in data:
        out["max_task_count"] = data["maxTaskCount"]
    if "autoScalingMetric" in data:
        import aws_sdk_ecs.types.express_gateway_service_scaling_metric

        out["auto_scaling_metric"] = (
            aws_sdk_ecs.types.express_gateway_service_scaling_metric.deserialize_aws_json_1_1(
                data["autoScalingMetric"]
            )
        )
    if "autoScalingTargetValue" in data:
        out["auto_scaling_target_value"] = data["autoScalingTargetValue"]
    return out
