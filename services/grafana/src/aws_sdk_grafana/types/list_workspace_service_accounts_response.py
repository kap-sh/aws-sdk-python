"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspaceServiceAccountsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.service_account_list
    import aws_sdk_grafana.types.workspace_id


class ListWorkspaceServiceAccountsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of service accounts.</p>"""
    service_accounts: "aws_sdk_grafana.types.service_account_list.ServiceAccountList"
    """<p>An array of structures containing information about the service accounts.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The workspace to which the service accounts are associated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceServiceAccountsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_grafana.types.service_account_list

    out["serviceAccounts"] = aws_sdk_grafana.types.service_account_list.serialize_json(
        value["service_accounts"]
    )
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> ListWorkspaceServiceAccountsResponse:
    out: ListWorkspaceServiceAccountsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "serviceAccounts" in data:
        import aws_sdk_grafana.types.service_account_list

        out["service_accounts"] = (
            aws_sdk_grafana.types.service_account_list.deserialize_json(
                data["serviceAccounts"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkspaceServiceAccountsResponse.service_accounts required"
        )
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError(
            "ListWorkspaceServiceAccountsResponse.workspace_id required"
        )
    return out
