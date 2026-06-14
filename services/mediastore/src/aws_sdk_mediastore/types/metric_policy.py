"""Generated from Smithy shape ``com.amazonaws.mediastore#MetricPolicy``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mediastore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mediastore.types.container_level_metrics
    import aws_sdk_mediastore.types.metric_policy_rules


class MetricPolicy(TypedDict):
    container_level_metrics: (
        "aws_sdk_mediastore.types.container_level_metrics.ContainerLevelMetrics"
    )
    """<p>A setting to enable or disable metrics at the container level.</p>"""
    metric_policy_rules: NotRequired[
        "aws_sdk_mediastore.types.metric_policy_rules.MetricPolicyRules"
    ]
    r"""<p>A parameter that holds an array of rules that enable metrics at the object level. This parameter is optional, but if you choose to include it, you must also include at least one rule. By default, you can include up to five rules. You can also <a href=\"https://console.aws.amazon.com/servicequotas/home?region=us-east-1#!/services/mediastore/quotas\">request a quota increase</a> to allow up to 300 rules per policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricPolicy) -> dict:
    out: dict = {}
    import aws_sdk_mediastore.types.container_level_metrics

    out["ContainerLevelMetrics"] = (
        aws_sdk_mediastore.types.container_level_metrics.serialize_aws_json_1_1(
            value["container_level_metrics"]
        )
    )
    if "metric_policy_rules" in value:
        import aws_sdk_mediastore.types.metric_policy_rules

        out["MetricPolicyRules"] = (
            aws_sdk_mediastore.types.metric_policy_rules.serialize_aws_json_1_1(
                value["metric_policy_rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MetricPolicy:
    out: MetricPolicy = {}  # type: ignore[typeddict-item]
    if "ContainerLevelMetrics" in data:
        import aws_sdk_mediastore.types.container_level_metrics

        out["container_level_metrics"] = (
            aws_sdk_mediastore.types.container_level_metrics.deserialize_aws_json_1_1(
                data["ContainerLevelMetrics"]
            )
        )
    else:
        raise DeserializationError("MetricPolicy.container_level_metrics required")
    if "MetricPolicyRules" in data:
        import aws_sdk_mediastore.types.metric_policy_rules

        out["metric_policy_rules"] = (
            aws_sdk_mediastore.types.metric_policy_rules.deserialize_aws_json_1_1(
                data["MetricPolicyRules"]
            )
        )
    return out
