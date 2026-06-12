"""Generated from Smithy shape ``com.amazonaws.devopsguru#ReactiveInsights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.reactive_insight_summary

ReactiveInsights: TypeAlias = list[
    "aws_sdk_devops_guru.types.reactive_insight_summary.ReactiveInsightSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReactiveInsights) -> list:
    import aws_sdk_devops_guru.types.reactive_insight_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.reactive_insight_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ReactiveInsights:
    import aws_sdk_devops_guru.types.reactive_insight_summary

    out: ReactiveInsights = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.reactive_insight_summary.deserialize_json(item)
        )
    return out
