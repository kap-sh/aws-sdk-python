"""Generated from Smithy shape ``com.amazonaws.sesv2#ListReputationEntitiesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.max_items
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.reputation_entity_filter


class ListReputationEntitiesRequest(TypedDict):
    filter: NotRequired[
        "aws_sdk_sesv2.types.reputation_entity_filter.ReputationEntityFilter"
    ]
    """<p>An object that contains filters to apply when listing reputation entities. You can filter by entity type, reputation impact, sending status, or entity reference prefix.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A token returned from a previous call to <code>ListReputationEntities</code> to indicate the position in the list of reputation entities.</p>"""
    page_size: NotRequired["aws_sdk_sesv2.types.max_items.MaxItems"]
    """<p>The number of results to show in a single call to <code>ListReputationEntities</code>. If the number of results is larger than the number you specified in this parameter, then the response includes a <code>NextToken</code> element, which you can use to obtain additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListReputationEntitiesRequest) -> dict:
    out: dict = {}
    if "filter" in value:
        import aws_sdk_sesv2.types.reputation_entity_filter

        out["Filter"] = aws_sdk_sesv2.types.reputation_entity_filter.serialize_json(
            value["filter"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "page_size" in value:
        out["PageSize"] = value["page_size"]
    return out


def deserialize_json(data: dict) -> ListReputationEntitiesRequest:
    out: ListReputationEntitiesRequest = {}  # type: ignore[typeddict-item]
    if "Filter" in data:
        import aws_sdk_sesv2.types.reputation_entity_filter

        out["filter"] = aws_sdk_sesv2.types.reputation_entity_filter.deserialize_json(
            data["Filter"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "PageSize" in data:
        out["page_size"] = data["PageSize"]
    return out
