"""Generated from Smithy shape ``com.amazonaws.devopsguru#SearchOrganizationInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.proactive_insights
    import capo_devops_guru.types.reactive_insights
    import capo_devops_guru.types.uuid_next_token


class SearchOrganizationInsightsResponse(TypedDict, closed=True):
    proactive_insights: NotRequired[
        "capo_devops_guru.types.proactive_insights.ProactiveInsights"
    ]
    """<p>An integer that specifies the number of open proactive insights in your Amazon Web Services account.</p>"""
    reactive_insights: NotRequired[
        "capo_devops_guru.types.reactive_insights.ReactiveInsights"
    ]
    """<p>An integer that specifies the number of open reactive insights in your Amazon Web Services account.</p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchOrganizationInsightsResponse) -> dict:
    out: dict = {}
    if "proactive_insights" in value:
        import capo_devops_guru.types.proactive_insights

        out["ProactiveInsights"] = (
            capo_devops_guru.types.proactive_insights.serialize_json(
                value["proactive_insights"]
            )
        )
    if "reactive_insights" in value:
        import capo_devops_guru.types.reactive_insights

        out["ReactiveInsights"] = (
            capo_devops_guru.types.reactive_insights.serialize_json(
                value["reactive_insights"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchOrganizationInsightsResponse:
    out: SearchOrganizationInsightsResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveInsights" in data:
        import capo_devops_guru.types.proactive_insights

        out["proactive_insights"] = (
            capo_devops_guru.types.proactive_insights.deserialize_json(
                data["ProactiveInsights"]
            )
        )
    if "ReactiveInsights" in data:
        import capo_devops_guru.types.reactive_insights

        out["reactive_insights"] = (
            capo_devops_guru.types.reactive_insights.deserialize_json(
                data["ReactiveInsights"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
