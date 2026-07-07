"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListOrganizationInsightsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.proactive_organization_insights
    import aws_sdk_devops_guru.types.reactive_organization_insights
    import aws_sdk_devops_guru.types.uuid_next_token


class ListOrganizationInsightsResponse(TypedDict, closed=True):
    proactive_insights: NotRequired[
        "aws_sdk_devops_guru.types.proactive_organization_insights.ProactiveOrganizationInsights"
    ]
    """<p>An integer that specifies the number of open proactive insights in your Amazon Web Services account.</p>"""
    reactive_insights: NotRequired[
        "aws_sdk_devops_guru.types.reactive_organization_insights.ReactiveOrganizationInsights"
    ]
    """<p>An integer that specifies the number of open reactive insights in your Amazon Web Services account.</p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOrganizationInsightsResponse) -> dict:
    out: dict = {}
    if "proactive_insights" in value:
        import aws_sdk_devops_guru.types.proactive_organization_insights

        out["ProactiveInsights"] = (
            aws_sdk_devops_guru.types.proactive_organization_insights.serialize_json(
                value["proactive_insights"]
            )
        )
    if "reactive_insights" in value:
        import aws_sdk_devops_guru.types.reactive_organization_insights

        out["ReactiveInsights"] = (
            aws_sdk_devops_guru.types.reactive_organization_insights.serialize_json(
                value["reactive_insights"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListOrganizationInsightsResponse:
    out: ListOrganizationInsightsResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveInsights" in data:
        import aws_sdk_devops_guru.types.proactive_organization_insights

        out["proactive_insights"] = (
            aws_sdk_devops_guru.types.proactive_organization_insights.deserialize_json(
                data["ProactiveInsights"]
            )
        )
    if "ReactiveInsights" in data:
        import aws_sdk_devops_guru.types.reactive_organization_insights

        out["reactive_insights"] = (
            aws_sdk_devops_guru.types.reactive_organization_insights.deserialize_json(
                data["ReactiveInsights"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
