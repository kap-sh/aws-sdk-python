"""Generated from Smithy shape ``com.amazonaws.qbusiness#SearchRelevantContentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.attribute_filter
    import capo_qbusiness.types.content_source
    import capo_qbusiness.types.max_results
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.query_text


class SearchRelevantContentRequest(TypedDict, closed=True):
    application_id: "capo_qbusiness.types.application_id.ApplicationId"
    """<p>The unique identifier of the Amazon Q Business application to search.</p>"""
    query_text: "capo_qbusiness.types.query_text.QueryText"
    """<p>The text to search for.</p>"""
    content_source: "capo_qbusiness.types.content_source.ContentSource"
    """<p>The source of content to search in.</p>"""
    attribute_filter: NotRequired[
        "capo_qbusiness.types.attribute_filter.AttributeFilter"
    ]
    max_results: "capo_qbusiness.types.max_results.MaxResults"
    """<p>The maximum number of results to return.</p>"""
    next_token: NotRequired["capo_qbusiness.types.next_token.NextToken"]
    """<p>The token for the next set of results. (You received this token from a previous call.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchRelevantContentRequest) -> dict:
    out: dict = {}
    out["queryText"] = value["query_text"]
    import capo_qbusiness.types.content_source

    out["contentSource"] = capo_qbusiness.types.content_source.serialize_json(
        value["content_source"]
    )
    if "attribute_filter" in value:
        import capo_qbusiness.types.attribute_filter

        out["attributeFilter"] = capo_qbusiness.types.attribute_filter.serialize_json(
            value["attribute_filter"]
        )
    out["maxResults"] = value.get("max_results", 10)
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchRelevantContentRequest:
    out: SearchRelevantContentRequest = {}  # type: ignore[typeddict-item]
    if "queryText" in data:
        out["query_text"] = data["queryText"]
    else:
        raise DeserializationError("SearchRelevantContentRequest.query_text required")
    if "contentSource" in data:
        import capo_qbusiness.types.content_source

        out["content_source"] = capo_qbusiness.types.content_source.deserialize_json(
            data["contentSource"]
        )
    else:
        raise DeserializationError(
            "SearchRelevantContentRequest.content_source required"
        )
    if "attributeFilter" in data:
        import capo_qbusiness.types.attribute_filter

        out["attribute_filter"] = (
            capo_qbusiness.types.attribute_filter.deserialize_json(
                data["attributeFilter"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    else:
        out["max_results"] = 10
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
