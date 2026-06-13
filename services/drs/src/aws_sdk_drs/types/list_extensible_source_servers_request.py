"""Generated from Smithy shape ``com.amazonaws.drs#ListExtensibleSourceServersRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_drs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_drs.types.account_id
    import aws_sdk_drs.types.max_results_replicating_source_servers
    import aws_sdk_drs.types.pagination_token


class ListExtensibleSourceServersRequest(TypedDict):
    staging_account_id: "aws_sdk_drs.types.account_id.AccountID"
    """<p>The Id of the staging Account to retrieve extensible source servers from.</p>"""
    max_results: NotRequired[
        "aws_sdk_drs.types.max_results_replicating_source_servers.MaxResultsReplicatingSourceServers"
    ]
    """<p>The maximum number of extensible source servers to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_drs.types.pagination_token.PaginationToken"]
    """<p>The token of the next extensible source server to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExtensibleSourceServersRequest) -> dict:
    out: dict = {}
    out["stagingAccountID"] = value["staging_account_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExtensibleSourceServersRequest:
    out: ListExtensibleSourceServersRequest = {}  # type: ignore[typeddict-item]
    if "stagingAccountID" in data:
        out["staging_account_id"] = data["stagingAccountID"]
    else:
        raise DeserializationError(
            "ListExtensibleSourceServersRequest.staging_account_id required"
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
