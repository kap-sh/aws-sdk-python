"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectionAliasPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.connection_alias_id
    import capo_workspaces.types.limit
    import capo_workspaces.types.pagination_token


class DescribeConnectionAliasPermissionsRequest(TypedDict, closed=True):
    alias_id: "capo_workspaces.types.connection_alias_id.ConnectionAliasId"
    """<p>The identifier of the connection alias.</p>"""
    next_token: NotRequired["capo_workspaces.types.pagination_token.PaginationToken"]
    """<p>If you received a <code>NextToken</code> from a previous call that was paginated, provide this token to receive the next set of results. </p>"""
    max_results: NotRequired["capo_workspaces.types.limit.Limit"]
    """<p>The maximum number of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionAliasPermissionsRequest) -> dict:
    out: dict = {}
    out["AliasId"] = value["alias_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionAliasPermissionsRequest:
    out: DescribeConnectionAliasPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    else:
        raise DeserializationError(
            "DescribeConnectionAliasPermissionsRequest.alias_id required"
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
