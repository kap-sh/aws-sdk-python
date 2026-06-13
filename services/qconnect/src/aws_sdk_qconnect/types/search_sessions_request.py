"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchSessionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.max_results
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.search_expression
    import aws_sdk_qconnect.types.uuid_or_arn


class SearchSessionsRequest(TypedDict):
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    search_expression: "aws_sdk_qconnect.types.search_expression.SearchExpression"
    """<p>The search expression to filter results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchSessionsRequest) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.search_expression

    out["searchExpression"] = aws_sdk_qconnect.types.search_expression.serialize_json(
        value["search_expression"]
    )
    return out


def deserialize_json(data: dict) -> SearchSessionsRequest:
    out: SearchSessionsRequest = {}  # type: ignore[typeddict-item]
    if "searchExpression" in data:
        import aws_sdk_qconnect.types.search_expression

        out["search_expression"] = (
            aws_sdk_qconnect.types.search_expression.deserialize_json(
                data["searchExpression"]
            )
        )
    else:
        raise DeserializationError("SearchSessionsRequest.search_expression required")
    return out
