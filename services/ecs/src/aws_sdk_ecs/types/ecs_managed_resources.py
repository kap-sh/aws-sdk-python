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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ECSManagedResources) -> dict:
    out: dict = {}
    if "ingress_paths" in value:
        import aws_sdk_ecs.types.managed_ingress_paths

        out["ingressPaths"] = (
            aws_sdk_ecs.types.managed_ingress_paths.serialize_aws_json_1_1(
                value["ingress_paths"]
            )
        )
    if "auto_scaling" in value:
        import aws_sdk_ecs.types.managed_auto_scaling

        out["autoScaling"] = (
            aws_sdk_ecs.types.managed_auto_scaling.serialize_aws_json_1_1(
                value["auto_scaling"]
            )
        )
    if "metric_alarms" in value:
        import aws_sdk_ecs.types.managed_metric_alarms

        out["metricAlarms"] = (
            aws_sdk_ecs.types.managed_metric_alarms.serialize_aws_json_1_1(
                value["metric_alarms"]
            )
        )
    if "service_security_groups" in value:
        import aws_sdk_ecs.types.managed_security_groups

        out["serviceSecurityGroups"] = (
            aws_sdk_ecs.types.managed_security_groups.serialize_aws_json_1_1(
                value["service_security_groups"]
            )
        )
    if "log_groups" in value:
        import aws_sdk_ecs.types.managed_log_groups

        out["logGroups"] = aws_sdk_ecs.types.managed_log_groups.serialize_aws_json_1_1(
            value["log_groups"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ECSManagedResources:
    out: ECSManagedResources = {}  # type: ignore[typeddict-item]
    if "ingressPaths" in data:
        import aws_sdk_ecs.types.managed_ingress_paths

        out["ingress_paths"] = (
            aws_sdk_ecs.types.managed_ingress_paths.deserialize_aws_json_1_1(
                data["ingressPaths"]
            )
        )
    if "autoScaling" in data:
        import aws_sdk_ecs.types.managed_auto_scaling

        out["auto_scaling"] = (
            aws_sdk_ecs.types.managed_auto_scaling.deserialize_aws_json_1_1(
                data["autoScaling"]
            )
        )
    if "metricAlarms" in data:
        import aws_sdk_ecs.types.managed_metric_alarms

        out["metric_alarms"] = (
            aws_sdk_ecs.types.managed_metric_alarms.deserialize_aws_json_1_1(
                data["metricAlarms"]
            )
        )
    if "serviceSecurityGroups" in data:
        import aws_sdk_ecs.types.managed_security_groups

        out["service_security_groups"] = (
            aws_sdk_ecs.types.managed_security_groups.deserialize_aws_json_1_1(
                data["serviceSecurityGroups"]
            )
        )
    if "logGroups" in data:
        import aws_sdk_ecs.types.managed_log_groups

        out["log_groups"] = (
            aws_sdk_ecs.types.managed_log_groups.deserialize_aws_json_1_1(
                data["logGroups"]
            )
        )
    return out
