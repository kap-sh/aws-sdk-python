"""Generated from Smithy shape ``com.amazonaws.devopsguru#ProactiveOrganizationInsights``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.proactive_organization_insight_summary

ProactiveOrganizationInsights: TypeAlias = list[
    "capo_devops_guru.types.proactive_organization_insight_summary.ProactiveOrganizationInsightSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProactiveOrganizationInsights) -> list:
    import capo_devops_guru.types.proactive_organization_insight_summary

    out: list = []
    for item in value:
        out.append(
            capo_devops_guru.types.proactive_organization_insight_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ProactiveOrganizationInsights:
    import capo_devops_guru.types.proactive_organization_insight_summary

    out: ProactiveOrganizationInsights = []
    for item in data:
        out.append(
            capo_devops_guru.types.proactive_organization_insight_summary.deserialize_json(
                item
            )
        )
    return out
