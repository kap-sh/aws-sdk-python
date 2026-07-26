"""Generated from Smithy shape ``com.amazonaws.qconnect#SearchMessageTemplatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.max_results
    import capo_qconnect.types.message_template_search_expression
    import capo_qconnect.types.next_token
    import capo_qconnect.types.uuid_or_arn


class SearchMessageTemplatesRequest(TypedDict, closed=True):
    knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>"""
    search_expression: "capo_qconnect.types.message_template_search_expression.MessageTemplateSearchExpression"
    """<p>The search expression for querying the message template.</p>"""
    next_token: NotRequired["capo_qconnect.types.next_token.NextToken"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>"""
    max_results: NotRequired["capo_qconnect.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchMessageTemplatesRequest) -> dict:
    out: dict = {}
    import capo_qconnect.types.message_template_search_expression

    out["searchExpression"] = (
        capo_qconnect.types.message_template_search_expression.serialize_json(
            value["search_expression"]
        )
    )
    return out


def deserialize_json(data: dict) -> SearchMessageTemplatesRequest:
    out: SearchMessageTemplatesRequest = {}  # type: ignore[typeddict-item]
    if "searchExpression" in data:
        import capo_qconnect.types.message_template_search_expression

        out["search_expression"] = (
            capo_qconnect.types.message_template_search_expression.deserialize_json(
                data["searchExpression"]
            )
        )
    else:
        raise DeserializationError(
            "SearchMessageTemplatesRequest.search_expression required"
        )
    return out
