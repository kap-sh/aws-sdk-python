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
