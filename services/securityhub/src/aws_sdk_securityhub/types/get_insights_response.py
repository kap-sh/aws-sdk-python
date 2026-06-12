"""Generated from Smithy shape ``com.amazonaws.securityhub#GetInsightsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.insight_list
    import aws_sdk_securityhub.types.next_token


class GetInsightsResponse(TypedDict):
    insights: NotRequired["aws_sdk_securityhub.types.insight_list.InsightList"]
    """<p>The insights returned by the operation.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The pagination token to use to request the next page of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightsResponse) -> dict:
    out: dict = {}
    if "insights" in value:
        import aws_sdk_securityhub.types.insight_list

        out["Insights"] = aws_sdk_securityhub.types.insight_list.serialize_json(
            value["insights"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetInsightsResponse:
    out: GetInsightsResponse = {}  # type: ignore[typeddict-item]
    if "Insights" in data:
        import aws_sdk_securityhub.types.insight_list

        out["insights"] = aws_sdk_securityhub.types.insight_list.deserialize_json(
            data["Insights"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
