"""Generated from Smithy shape ``com.amazonaws.ecs#ECSManagedResources``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.managed_auto_scaling
    import aws_sdk_ecs.types.managed_ingress_paths
    import aws_sdk_ecs.types.managed_log_groups
    import aws_sdk_ecs.types.managed_metric_alarms
    import aws_sdk_ecs.types.managed_security_groups


class ECSManagedResources(TypedDict):
    ingress_paths: NotRequired[
        "aws_sdk_ecs.types.managed_ingress_paths.ManagedIngressPaths"
    ]
    """<p>The ingress paths and endpoints for the Express service.</p>"""
    auto_scaling: NotRequired[
        "aws_sdk_ecs.types.managed_auto_scaling.ManagedAutoScaling"
    ]
    """<p>The auto-scaling configuration and policies for the Express service.</p>"""
    metric_alarms: NotRequired[
        "aws_sdk_ecs.types.managed_metric_alarms.ManagedMetricAlarms"
    ]
    """<p>The CloudWatch metric alarms associated with the Express service.</p>"""
    service_security_groups: NotRequired[
        "aws_sdk_ecs.types.managed_security_groups.ManagedSecurityGroups"
    ]
    """<p>The security groups managed by the Express service.</p>"""
    log_groups: NotRequired["aws_sdk_ecs.types.managed_log_groups.ManagedLogGroups"]
    """<p>The log groups managed by the Express service.</p>"""
