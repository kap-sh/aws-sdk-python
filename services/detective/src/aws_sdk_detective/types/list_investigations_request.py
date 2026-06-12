"""Generated from Smithy shape ``com.amazonaws.detective#ListInvestigationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_detective.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_detective.types.ai_pagination_token
    import aws_sdk_detective.types.filter_criteria
    import aws_sdk_detective.types.graph_arn
    import aws_sdk_detective.types.max_results
    import aws_sdk_detective.types.sort_criteria


class ListInvestigationsRequest(TypedDict):
    graph_arn: "aws_sdk_detective.types.graph_arn.GraphArn"
    """<p>The Amazon Resource Name (ARN) of the behavior graph.</p>"""
    next_token: NotRequired[
        "aws_sdk_detective.types.ai_pagination_token.AiPaginationToken"
    ]
    """<p>Lists if there are more results available. The value of nextToken is a unique pagination token for each page. Repeat the call using the returned token to retrieve the next page. Keep all other arguments unchanged.</p> <p>Each pagination token expires after 24 hours. Using an expired pagination token will return a Validation Exception error.</p>"""
    max_results: NotRequired["aws_sdk_detective.types.max_results.MaxResults"]
    """<p>Lists the maximum number of investigations in a page.</p>"""
    filter_criteria: NotRequired[
        "aws_sdk_detective.types.filter_criteria.FilterCriteria"
    ]
    """<p>Filters the investigation results based on a criteria.</p>"""
    sort_criteria: NotRequired["aws_sdk_detective.types.sort_criteria.SortCriteria"]
    """<p>Sorts the investigation results based on a criteria.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListInvestigationsRequest) -> dict:
    out: dict = {}
    out["GraphArn"] = value["graph_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter_criteria" in value:
        import aws_sdk_detective.types.filter_criteria

        out["FilterCriteria"] = aws_sdk_detective.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "sort_criteria" in value:
        import aws_sdk_detective.types.sort_criteria

        out["SortCriteria"] = aws_sdk_detective.types.sort_criteria.serialize_json(
            value["sort_criteria"]
        )
    return out


def deserialize_json(data: dict) -> ListInvestigationsRequest:
    out: ListInvestigationsRequest = {}  # type: ignore[typeddict-item]
    if "GraphArn" in data:
        out["graph_arn"] = data["GraphArn"]
    else:
        raise DeserializationError("ListInvestigationsRequest.graph_arn required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "FilterCriteria" in data:
        import aws_sdk_detective.types.filter_criteria

        out["filter_criteria"] = (
            aws_sdk_detective.types.filter_criteria.deserialize_json(
                data["FilterCriteria"]
            )
        )
    if "SortCriteria" in data:
        import aws_sdk_detective.types.sort_criteria

        out["sort_criteria"] = aws_sdk_detective.types.sort_criteria.deserialize_json(
            data["SortCriteria"]
        )
    return out
