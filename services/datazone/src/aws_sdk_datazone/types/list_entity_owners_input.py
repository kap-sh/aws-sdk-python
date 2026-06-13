"""Generated from Smithy shape ``com.amazonaws.datazone#ListEntityOwnersInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_zone_entity_type
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.max_results_for_list_domains
    import aws_sdk_datazone.types.pagination_token


class ListEntityOwnersInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list entity owners.</p>"""
    entity_type: "aws_sdk_datazone.types.data_zone_entity_type.DataZoneEntityType"
    """<p>The type of the entity that you want to list.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity that you want to list.</p>"""
    max_results: NotRequired[
        "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
    ]
    """<p>The maximum number of entities to return in a single call to <code>ListEntityOwners</code>. When the number of entities to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of entities is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of entities, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListEntityOwners</code> to list the next set of entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEntityOwnersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListEntityOwnersInput:
    out: ListEntityOwnersInput = {}  # type: ignore[typeddict-item]
    return out
