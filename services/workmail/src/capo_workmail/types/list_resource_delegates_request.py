"""Generated from Smithy shape ``com.amazonaws.workmail#ListResourceDelegatesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.entity_identifier
    import capo_workmail.types.max_results
    import capo_workmail.types.next_token
    import capo_workmail.types.organization_id


class ListResourceDelegatesRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization that contains the resource for which delegates are listed.</p>"""
    resource_id: "capo_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the resource whose delegates are listed.</p> <p>The identifier can accept <i>ResourceId</i>, <i>Resourcename</i>, or <i>email</i>. The following identity formats are available:</p> <ul> <li> <p>Resource ID: r-0123456789a0123456789b0123456789</p> </li> <li> <p>Email address: resource@domain.tld</p> </li> <li> <p>Resource name: resource</p> </li> </ul>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token used to paginate through the delegates associated with a resource.</p>"""
    max_results: NotRequired["capo_workmail.types.max_results.MaxResults"]
    """<p>The number of maximum results in a page.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResourceDelegatesRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["ResourceId"] = value["resource_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResourceDelegatesRequest:
    out: ListResourceDelegatesRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "ListResourceDelegatesRequest.organization_id required"
        )
    if "ResourceId" in data:
        out["resource_id"] = data["ResourceId"]
    else:
        raise DeserializationError("ListResourceDelegatesRequest.resource_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
