"""Generated from Smithy shape ``com.amazonaws.kendra#GetQuerySuggestionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kendra.types.query_suggestions_id
    import aws_sdk_kendra.types.suggestion_list


class GetQuerySuggestionsResponse(TypedDict):
    query_suggestions_id: NotRequired[
        "aws_sdk_kendra.types.query_suggestions_id.QuerySuggestionsId"
    ]
    """<p>The identifier for a list of query suggestions for an index.</p>"""
    suggestions: NotRequired["aws_sdk_kendra.types.suggestion_list.SuggestionList"]
    """<p>A list of query suggestions for an index.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQuerySuggestionsResponse) -> dict:
    out: dict = {}
    if "query_suggestions_id" in value:
        out["QuerySuggestionsId"] = value["query_suggestions_id"]
    if "suggestions" in value:
        import aws_sdk_kendra.types.suggestion_list

        out["Suggestions"] = (
            aws_sdk_kendra.types.suggestion_list.serialize_aws_json_1_1(
                value["suggestions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQuerySuggestionsResponse:
    out: GetQuerySuggestionsResponse = {}  # type: ignore[typeddict-item]
    if "QuerySuggestionsId" in data:
        out["query_suggestions_id"] = data["QuerySuggestionsId"]
    if "Suggestions" in data:
        import aws_sdk_kendra.types.suggestion_list

        out["suggestions"] = (
            aws_sdk_kendra.types.suggestion_list.deserialize_aws_json_1_1(
                data["Suggestions"]
            )
        )
    return out
