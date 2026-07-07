"""Generated from Smithy shape ``com.amazonaws.workmail#ListGroupsForEntityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmail.types.entity_identifier
    import aws_sdk_workmail.types.list_groups_for_entity_filters
    import aws_sdk_workmail.types.max_results
    import aws_sdk_workmail.types.next_token
    import aws_sdk_workmail.types.organization_id


class ListGroupsForEntityRequest(TypedDict, closed=True):
    organization_id: "aws_sdk_workmail.types.organization_id.OrganizationId"
    """<p>The identifier for the organization under which the entity exists.</p>"""
    entity_id: "aws_sdk_workmail.types.entity_identifier.EntityIdentifier"
    """<p>The identifier for the entity.</p> <p>The entity ID can accept <i>UserId or GroupID</i>, <i>Username or Groupname</i>, or <i>email</i>.</p> <ul> <li> <p>Entity ID: 12345678-1234-1234-1234-123456789012 or S-1-1-12-1234567890-123456789-123456789-1234</p> </li> <li> <p>Email address: entity@domain.tld</p> </li> <li> <p>Entity name: entity</p> </li> </ul>"""
    filters: NotRequired[
        "aws_sdk_workmail.types.list_groups_for_entity_filters.ListGroupsForEntityFilters"
    ]
    """<p>Limit the search results based on the filter criteria.</p>"""
    next_token: NotRequired["aws_sdk_workmail.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results. The first call does not contain any tokens.</p>"""
    max_results: NotRequired["aws_sdk_workmail.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in a single call.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGroupsForEntityRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    out["EntityId"] = value["entity_id"]
    if "filters" in value:
        import aws_sdk_workmail.types.list_groups_for_entity_filters

        out["Filters"] = (
            aws_sdk_workmail.types.list_groups_for_entity_filters.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGroupsForEntityRequest:
    out: ListGroupsForEntityRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "ListGroupsForEntityRequest.organization_id required"
        )
    if "EntityId" in data:
        out["entity_id"] = data["EntityId"]
    else:
        raise DeserializationError("ListGroupsForEntityRequest.entity_id required")
    if "Filters" in data:
        import aws_sdk_workmail.types.list_groups_for_entity_filters

        out["filters"] = (
            aws_sdk_workmail.types.list_groups_for_entity_filters.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
