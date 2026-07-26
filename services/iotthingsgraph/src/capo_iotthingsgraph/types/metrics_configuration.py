"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#MetricsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.enabled
    import capo_iotthingsgraph.types.role_arn


class MetricsConfiguration(TypedDict, closed=True):
    cloud_metric_enabled: "capo_iotthingsgraph.types.enabled.Enabled"
    """<p>A Boolean that specifies whether cloud metrics are collected.</p>"""
    metric_rule_role_arn: NotRequired["capo_iotthingsgraph.types.role_arn.RoleArn"]
    """<p>The ARN of the role that is used to collect cloud metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricsConfiguration) -> dict:
    out: dict = {}
    out["cloudMetricEnabled"] = value.get("cloud_metric_enabled", False)
    if "metric_rule_role_arn" in value:
        out["metricRuleRoleArn"] = value["metric_rule_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricsConfiguration:
    out: MetricsConfiguration = {}  # type: ignore[typeddict-item]
    if "cloudMetricEnabled" in data:
        out["cloud_metric_enabled"] = data["cloudMetricEnabled"]
    else:
        out["cloud_metric_enabled"] = False
    if "metricRuleRoleArn" in data:
        out["metric_rule_role_arn"] = data["metricRuleRoleArn"]
    return out
