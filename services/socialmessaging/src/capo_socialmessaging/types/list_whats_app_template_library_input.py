"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppTemplateLibraryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.filter
    import capo_socialmessaging.types.linked_whats_app_business_account_id
    import capo_socialmessaging.types.max_results
    import capo_socialmessaging.types.next_token


class ListWhatsAppTemplateLibraryInput(TypedDict, closed=True):
    next_token: NotRequired["capo_socialmessaging.types.next_token.NextToken"]
    """<p>The token for the next page of results.</p>"""
    max_results: NotRequired["capo_socialmessaging.types.max_results.MaxResults"]
    """<p>The maximum number of results to return per page (1-100).</p>"""
    id: "capo_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account to list library templates for.</p>"""
    filters: NotRequired["capo_socialmessaging.types.filter.Filter"]
    """<p>Map of filters to apply (searchKey, topic, usecase, industry, language).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppTemplateLibraryInput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "filters" in value:
        import capo_socialmessaging.types.filter

        out["filters"] = capo_socialmessaging.types.filter.serialize_json(
            value["filters"]
        )
    return out


def deserialize_json(data: dict) -> ListWhatsAppTemplateLibraryInput:
    out: ListWhatsAppTemplateLibraryInput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "filters" in data:
        import capo_socialmessaging.types.filter

        out["filters"] = capo_socialmessaging.types.filter.deserialize_json(
            data["filters"]
        )
    return out
