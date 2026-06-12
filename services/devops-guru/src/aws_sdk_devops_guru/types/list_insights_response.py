"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListInsightsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.proactive_insights
    import aws_sdk_devops_guru.types.reactive_insights
    import aws_sdk_devops_guru.types.uuid_next_token


class ListInsightsResponse(TypedDict):
    proactive_insights: NotRequired[
        "aws_sdk_devops_guru.types.proactive_insights.ProactiveInsights"
    ]
    """<p> The returned list of proactive insights. </p>"""
    reactive_insights: NotRequired[
        "aws_sdk_devops_guru.types.reactive_insights.ReactiveInsights"
    ]
    """<p> The returned list of reactive insights. </p>"""
    next_token: NotRequired["aws_sdk_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInsightsResponse) -> dict:
    out: dict = {}
    if "proactive_insights" in value:
        import aws_sdk_devops_guru.types.proactive_insights

        out["ProactiveInsights"] = (
            aws_sdk_devops_guru.types.proactive_insights.serialize_json(
                value["proactive_insights"]
            )
        )
    if "reactive_insights" in value:
        import aws_sdk_devops_guru.types.reactive_insights

        out["ReactiveInsights"] = (
            aws_sdk_devops_guru.types.reactive_insights.serialize_json(
                value["reactive_insights"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListInsightsResponse:
    out: ListInsightsResponse = {}  # type: ignore[typeddict-item]
    if "ProactiveInsights" in data:
        import aws_sdk_devops_guru.types.proactive_insights

        out["proactive_insights"] = (
            aws_sdk_devops_guru.types.proactive_insights.deserialize_json(
                data["ProactiveInsights"]
            )
        )
    if "ReactiveInsights" in data:
        import aws_sdk_devops_guru.types.reactive_insights

        out["reactive_insights"] = (
            aws_sdk_devops_guru.types.reactive_insights.deserialize_json(
                data["ReactiveInsights"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
