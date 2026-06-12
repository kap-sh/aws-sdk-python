"""Generated from Smithy shape ``com.amazonaws.mpa#ListSessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.approval_team_arn
    import aws_sdk_mpa.types.filters
    import aws_sdk_mpa.types.max_results
    import aws_sdk_mpa.types.token


class ListSessionsRequest(TypedDict):
    approval_team_arn: "aws_sdk_mpa.types.approval_team_arn.ApprovalTeamArn"
    """<p>Amazon Resource Name (ARN) for the approval team.</p>"""
    max_results: "aws_sdk_mpa.types.max_results.MaxResults"
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""
    next_token: NotRequired["aws_sdk_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    filters: NotRequired["aws_sdk_mpa.types.filters.Filters"]
    """<p>An array of <code>Filter</code> objects. Contains the filter to apply when listing sessions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListSessionsRequest) -> dict:
    out: dict = {}
    out["MaxResults"] = value.get("max_results", 20)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "filters" in value:
        import aws_sdk_mpa.types.filters

        out["Filters"] = aws_sdk_mpa.types.filters.serialize_json(value["filters"])
    return out


def deserialize_json(data: dict) -> ListSessionsRequest:
    out: ListSessionsRequest = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 20
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Filters" in data:
        import aws_sdk_mpa.types.filters

        out["filters"] = aws_sdk_mpa.types.filters.deserialize_json(data["Filters"])
    return out
