"""Generated from Smithy shape ``com.amazonaws.devopsguru#ProactiveInsights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.proactive_insight_summary

ProactiveInsights: TypeAlias = list[
    "aws_sdk_devops_guru.types.proactive_insight_summary.ProactiveInsightSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveInsights) -> list:
    import aws_sdk_devops_guru.types.proactive_insight_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.proactive_insight_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProactiveInsights:
    import aws_sdk_devops_guru.types.proactive_insight_summary

    out: ProactiveInsights = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.proactive_insight_summary.deserialize_json(item)
        )
    return out
