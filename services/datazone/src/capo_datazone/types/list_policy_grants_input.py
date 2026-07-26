"""Generated from Smithy shape ``com.amazonaws.datazone#ListPolicyGrantsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.managed_policy_type
    import capo_datazone.types.max_results_for_list_domains
    import capo_datazone.types.pagination_token
    import capo_datazone.types.target_entity_type


class ListPolicyGrantsInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list policy grants.</p>"""
    entity_type: "capo_datazone.types.target_entity_type.TargetEntityType"
    """<p>The type of entity for which you want to list policy grants.</p>"""
    entity_identifier: "str"
    """<p>The ID of the entity for which you want to list policy grants.</p>"""
    policy_type: "capo_datazone.types.managed_policy_type.ManagedPolicyType"
    """<p>The type of policy that you want to list.</p>"""
    max_results: NotRequired[
        "capo_datazone.types.max_results_for_list_domains.MaxResultsForListDomains"
    ]
    """<p>The maximum number of grants to return in a single call to <code>ListPolicyGrants</code>. When the number of grants to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListPolicyGrants</code> to list the next set of grants.</p>"""
    next_token: NotRequired["capo_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of grants is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of grants, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListPolicyGrants</code> to list the next set of grants.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyGrantsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyGrantsInput:
    out: ListPolicyGrantsInput = {}  # type: ignore[typeddict-item]
    return out
