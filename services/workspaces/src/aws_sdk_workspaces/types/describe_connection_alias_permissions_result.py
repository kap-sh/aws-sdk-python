"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeConnectionAliasPermissionsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.connection_alias_id
    import aws_sdk_workspaces.types.connection_alias_permissions
    import aws_sdk_workspaces.types.pagination_token


class DescribeConnectionAliasPermissionsResult(TypedDict):
    alias_id: NotRequired[
        "aws_sdk_workspaces.types.connection_alias_id.ConnectionAliasId"
    ]
    """<p>The identifier of the connection alias.</p>"""
    connection_alias_permissions: NotRequired[
        "aws_sdk_workspaces.types.connection_alias_permissions.ConnectionAliasPermissions"
    ]
    """<p>The permissions associated with a connection alias.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConnectionAliasPermissionsResult) -> dict:
    out: dict = {}
    if "alias_id" in value:
        out["AliasId"] = value["alias_id"]
    if "connection_alias_permissions" in value:
        import aws_sdk_workspaces.types.connection_alias_permissions

        out["ConnectionAliasPermissions"] = (
            aws_sdk_workspaces.types.connection_alias_permissions.serialize_aws_json_1_1(
                value["connection_alias_permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConnectionAliasPermissionsResult:
    out: DescribeConnectionAliasPermissionsResult = {}  # type: ignore[typeddict-item]
    if "AliasId" in data:
        out["alias_id"] = data["AliasId"]
    if "ConnectionAliasPermissions" in data:
        import aws_sdk_workspaces.types.connection_alias_permissions

        out["connection_alias_permissions"] = (
            aws_sdk_workspaces.types.connection_alias_permissions.deserialize_aws_json_1_1(
                data["ConnectionAliasPermissions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
