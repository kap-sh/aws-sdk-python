"""Generated from Smithy shape ``com.amazonaws.devopsguru#ReactiveOrganizationInsights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.reactive_organization_insight_summary

ReactiveOrganizationInsights: TypeAlias = list[
    "aws_sdk_devops_guru.types.reactive_organization_insight_summary.ReactiveOrganizationInsightSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ReactiveOrganizationInsights) -> list:
    import aws_sdk_devops_guru.types.reactive_organization_insight_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_devops_guru.types.reactive_organization_insight_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ReactiveOrganizationInsights:
    import aws_sdk_devops_guru.types.reactive_organization_insight_summary

    out: ReactiveOrganizationInsights = []
    for item in data:
        out.append(
            aws_sdk_devops_guru.types.reactive_organization_insight_summary.deserialize_json(
                item
            )
        )
    return out
