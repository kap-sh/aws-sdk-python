"""Generated from Smithy shape ``com.amazonaws.grafana#ListWorkspaceServiceAccountTokensResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.service_account_token_list
    import aws_sdk_grafana.types.workspace_id


class ListWorkspaceServiceAccountTokensResponse(TypedDict):
    next_token: NotRequired["aws_sdk_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of service accounts.</p>"""
    service_account_tokens: (
        "aws_sdk_grafana.types.service_account_token_list.ServiceAccountTokenList"
    )
    """<p>An array of structures containing information about the tokens.</p>"""
    service_account_id: "str"
    """<p>The ID of the service account where the tokens reside.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace where the tokens reside.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWorkspaceServiceAccountTokensResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_grafana.types.service_account_token_list

    out["serviceAccountTokens"] = (
        aws_sdk_grafana.types.service_account_token_list.serialize_json(
            value["service_account_tokens"]
        )
    )
    out["serviceAccountId"] = value["service_account_id"]
    out["workspaceId"] = value["workspace_id"]
    return out


def deserialize_json(data: dict) -> ListWorkspaceServiceAccountTokensResponse:
    out: ListWorkspaceServiceAccountTokensResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "serviceAccountTokens" in data:
        import aws_sdk_grafana.types.service_account_token_list

        out["service_account_tokens"] = (
            aws_sdk_grafana.types.service_account_token_list.deserialize_json(
                data["serviceAccountTokens"]
            )
        )
    else:
        raise DeserializationError(
            "ListWorkspaceServiceAccountTokensResponse.service_account_tokens required"
        )
    if "serviceAccountId" in data:
        out["service_account_id"] = data["serviceAccountId"]
    else:
        raise DeserializationError(
            "ListWorkspaceServiceAccountTokensResponse.service_account_id required"
        )
    if "workspaceId" in data:
        out["workspace_id"] = data["workspaceId"]
    else:
        raise DeserializationError(
            "ListWorkspaceServiceAccountTokensResponse.workspace_id required"
        )
    return out
