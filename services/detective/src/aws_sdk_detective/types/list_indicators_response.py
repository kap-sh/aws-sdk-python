"""Generated from Smithy shape ``com.amazonaws.detective#ListIndicatorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_detective.types.ai_pagination_token
    import aws_sdk_detective.types.graph_arn
    import aws_sdk_detective.types.indicators
    import aws_sdk_detective.types.investigation_id


class ListIndicatorsResponse(TypedDict, closed=True):
    graph_arn: NotRequired["aws_sdk_detective.types.graph_arn.GraphArn"]
    """<p>The Amazon Resource Name (ARN) of the behavior graph.</p>"""
    investigation_id: NotRequired[
        "aws_sdk_detective.types.investigation_id.InvestigationId"
    ]
    """<p>The investigation ID of the investigation report.</p>"""
    next_token: NotRequired[
        "aws_sdk_detective.types.ai_pagination_token.AiPaginationToken"
    ]
    """<p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.</p>"""
    indicators: NotRequired["aws_sdk_detective.types.indicators.Indicators"]
    """<p>Lists the indicators of compromise.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListIndicatorsResponse) -> dict:
    out: dict = {}
    if "graph_arn" in value:
        out["GraphArn"] = value["graph_arn"]
    if "investigation_id" in value:
        out["InvestigationId"] = value["investigation_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "indicators" in value:
        import aws_sdk_detective.types.indicators

        out["Indicators"] = aws_sdk_detective.types.indicators.serialize_json(
            value["indicators"]
        )
    return out


def deserialize_json(data: dict) -> ListIndicatorsResponse:
    out: ListIndicatorsResponse = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    if "InvestigationId" in data:
        out["investigation_id"] = data["InvestigationId"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Indicators" in data:
        import aws_sdk_detective.types.indicators

        out["indicators"] = aws_sdk_detective.types.indicators.deserialize_json(
            data["Indicators"]
        )
    return out
