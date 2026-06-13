"""Generated from Smithy shape ``com.amazonaws.qconnect#QueryAssistantResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.next_token
    import aws_sdk_qconnect.types.query_results_list


class QueryAssistantResponse(TypedDict):
    results: "aws_sdk_qconnect.types.query_results_list.QueryResultsList"
    """<p>The results of the query.</p>"""
    next_token: NotRequired["aws_sdk_qconnect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryAssistantResponse) -> dict:
    out: dict = {}
    import aws_sdk_qconnect.types.query_results_list

    out["results"] = aws_sdk_qconnect.types.query_results_list.serialize_json(
        value["results"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> QueryAssistantResponse:
    out: QueryAssistantResponse = {}  # type: ignore[typeddict-item]
    if "results" in data:
        import aws_sdk_qconnect.types.query_results_list

        out["results"] = aws_sdk_qconnect.types.query_results_list.deserialize_json(
            data["results"]
        )
    else:
        raise DeserializationError("QueryAssistantResponse.results required")
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
