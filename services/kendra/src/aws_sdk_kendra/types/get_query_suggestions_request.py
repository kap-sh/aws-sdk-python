"""Generated from Smithy shape ``com.amazonaws.kendra#GetQuerySuggestionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.attribute_suggestions_get_config
    import aws_sdk_kendra.types.index_id
    import aws_sdk_kendra.types.integer
    import aws_sdk_kendra.types.suggestion_query_text
    import aws_sdk_kendra.types.suggestion_types


class GetQuerySuggestionsRequest(TypedDict):
    index_id: "aws_sdk_kendra.types.index_id.IndexId"
    """<p>The identifier of the index you want to get query suggestions from.</p>"""
    query_text: "aws_sdk_kendra.types.suggestion_query_text.SuggestionQueryText"
    """<p>The text of a user's query to generate query suggestions.</p> <p>A query is suggested if the query prefix matches what a user starts to type as their query.</p> <p>Amazon Kendra does not show any suggestions if a user types fewer than two characters or more than 60 characters. A query must also have at least one search result and contain at least one word of more than four characters.</p>"""
    max_suggestions_count: NotRequired["aws_sdk_kendra.types.integer.Integer"]
    """<p>The maximum number of query suggestions you want to show to your users.</p>"""
    suggestion_types: NotRequired[
        "aws_sdk_kendra.types.suggestion_types.SuggestionTypes"
    ]
    """<p>The suggestions type to base query suggestions on. The suggestion types are query history or document fields/attributes. You can set one type or the other.</p> <p>If you set query history as your suggestions type, Amazon Kendra suggests queries relevant to your users based on popular queries in the query history.</p> <p>If you set document fields/attributes as your suggestions type, Amazon Kendra suggests queries relevant to your users based on the contents of document fields.</p>"""
    attribute_suggestions_config: NotRequired[
        "aws_sdk_kendra.types.attribute_suggestions_get_config.AttributeSuggestionsGetConfig"
    ]
    """<p>Configuration information for the document fields/attributes that you want to base query suggestions on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetQuerySuggestionsRequest) -> dict:
    out: dict = {}
    out["IndexId"] = value["index_id"]
    out["QueryText"] = value["query_text"]
    if "max_suggestions_count" in value:
        out["MaxSuggestionsCount"] = value["max_suggestions_count"]
    if "suggestion_types" in value:
        import aws_sdk_kendra.types.suggestion_types

        out["SuggestionTypes"] = (
            aws_sdk_kendra.types.suggestion_types.serialize_aws_json_1_1(
                value["suggestion_types"]
            )
        )
    if "attribute_suggestions_config" in value:
        import aws_sdk_kendra.types.attribute_suggestions_get_config

        out["AttributeSuggestionsConfig"] = (
            aws_sdk_kendra.types.attribute_suggestions_get_config.serialize_aws_json_1_1(
                value["attribute_suggestions_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetQuerySuggestionsRequest:
    out: GetQuerySuggestionsRequest = {}  # type: ignore[typeddict-item]
    if "IndexId" in data:
        out["index_id"] = data["IndexId"]
    else:
        raise DeserializationError("GetQuerySuggestionsRequest.index_id required")
    if "QueryText" in data:
        out["query_text"] = data["QueryText"]
    else:
        raise DeserializationError("GetQuerySuggestionsRequest.query_text required")
    if "MaxSuggestionsCount" in data:
        out["max_suggestions_count"] = data["MaxSuggestionsCount"]
    if "SuggestionTypes" in data:
        import aws_sdk_kendra.types.suggestion_types

        out["suggestion_types"] = (
            aws_sdk_kendra.types.suggestion_types.deserialize_aws_json_1_1(
                data["SuggestionTypes"]
            )
        )
    if "AttributeSuggestionsConfig" in data:
        import aws_sdk_kendra.types.attribute_suggestions_get_config

        out["attribute_suggestions_config"] = (
            aws_sdk_kendra.types.attribute_suggestions_get_config.deserialize_aws_json_1_1(
                data["AttributeSuggestionsConfig"]
            )
        )
    return out
