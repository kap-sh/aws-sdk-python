"""Generated from Smithy shape ``com.amazonaws.grafana#ListPermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_grafana.types.pagination_token
    import aws_sdk_grafana.types.sso_id
    import aws_sdk_grafana.types.user_type
    import aws_sdk_grafana.types.workspace_id

class ListPermissionsRequest(TypedDict):
    max_results: NotRequired["int"]
    """<p>The maximum number of results to include in the response.</p>"""
    next_token: NotRequired["aws_sdk_grafana.types.pagination_token.PaginationToken"]
    """<p>The token to use when requesting the next set of results. You received this token from a previous <code>ListPermissions</code> operation.</p>"""
    user_type: NotRequired["aws_sdk_grafana.types.user_type.UserType"]
    """<p>(Optional) If you specify <code>SSO_USER</code>, then only the permissions of IAM Identity Center users are returned. If you specify <code>SSO_GROUP</code>, only the permissions of IAM Identity Center groups are returned.</p>"""
    user_id: NotRequired["aws_sdk_grafana.types.sso_id.SsoId"]
    """<p>(Optional) Limits the results to only the user that matches this ID.</p>"""
    group_id: NotRequired["aws_sdk_grafana.types.sso_id.SsoId"]
    """<p>(Optional) Limits the results to only the group that matches this ID.</p>"""
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to list permissions for. This parameter is required.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPermissionsRequest:
    out: ListPermissionsRequest = {}  # type: ignore[typeddict-item]
    return out