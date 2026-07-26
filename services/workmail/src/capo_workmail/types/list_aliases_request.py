"""Generated from Smithy shape ``com.amazonaws.workmail#ListAliasesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.max_results
    import capo_workmail.types.next_token
    import capo_workmail.types.organization_id
    import capo_workmail.types.work_mail_identifier


class ListAliasesRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the entity exists.</p>"""
    entity_id: "capo_workmail.types.work_mail_identifier.WorkMailIdentifier"
    """<p>The identifier for the entity for which to list the aliases.</p>"""
    next_token: NotRequired["capo_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>"""
    max_results: NotRequired["capo_workmail.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAliasesRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAliasesRequest:
    out: ListAliasesRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError("ListAliasesRequest.organization_id required")
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("ListAliasesRequest.entity_id required")
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
