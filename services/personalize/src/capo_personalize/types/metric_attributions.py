"""Generated from Smithy shape ``com.amazonaws.personalize#MetricAttributions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_personalize.types.metric_attribution_summary

MetricAttributions: TypeAlias = list[
    "capo_personalize.types.metric_attribution_summary.MetricAttributionSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricAttributions) -> list:
    import capo_personalize.types.metric_attribution_summary

    out: list = []
    for item in value:
        out.append(
            capo_personalize.types.metric_attribution_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MetricAttributions:
    import capo_personalize.types.metric_attribution_summary

    out: MetricAttributions = []
    for item in data:
        out.append(
            capo_personalize.types.metric_attribution_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
