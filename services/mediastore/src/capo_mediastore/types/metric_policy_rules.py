"""Generated from Smithy shape ``com.amazonaws.mediastore#MetricPolicyRules``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediastore.types.metric_policy_rule

MetricPolicyRules: TypeAlias = list[
    "capo_mediastore.types.metric_policy_rule.MetricPolicyRule"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricPolicyRules) -> list:
    import capo_mediastore.types.metric_policy_rule

    out: list = []
    for item in value:
        out.append(
            capo_mediastore.types.metric_policy_rule.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricPolicyRules:
    import capo_mediastore.types.metric_policy_rule

    out: MetricPolicyRules = []
    for item in data:
        out.append(
            capo_mediastore.types.metric_policy_rule.deserialize_aws_json_1_1(item)
        )
    return out
