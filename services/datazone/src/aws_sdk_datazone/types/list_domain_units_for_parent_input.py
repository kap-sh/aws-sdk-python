"""Generated from Smithy shape ``com.amazonaws.datazone#ListDomainUnitsForParentInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.domain_unit_id
    import aws_sdk_datazone.types.max_results_for_list_domains
    import aws_sdk_datazone.types.pagination_token


class ListDomainUnitsForParentInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain in which you want to list domain units for a parent domain unit.</p>"""
    parent_domain_unit_identifier: "aws_sdk_datazone.types.domain_unit_id.DomainUnitId"
    """<p>The ID of the parent domain unit.</p>"""
    max_results: NotRequired[
        "aws_sdk_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
    ]
    """<p>The maximum number of domain units to return in a single call to ListDomainUnitsForParent. When the number of domain units to be listed is greater than the value of MaxResults, the response contains a NextToken value that you can use in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of domain units is greater than the default value for the MaxResults parameter, or if you explicitly specify a value for MaxResults that is less than the number of domain units, the response includes a pagination token named NextToken. You can specify this NextToken value in a subsequent call to ListDomainUnitsForParent to list the next set of domain units.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDomainUnitsForParentInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDomainUnitsForParentInput:
    out: ListDomainUnitsForParentInput = {}  # type: ignore[typeddict-item]
    return out
