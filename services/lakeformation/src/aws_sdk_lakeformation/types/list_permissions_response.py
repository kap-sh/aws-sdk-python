"""Generated from Smithy shape ``com.amazonaws.lakeformation#ListPermissionsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.principal_resource_permissions_list
    import aws_sdk_lakeformation.types.token


class ListPermissionsResponse(TypedDict):
    principal_resource_permissions: NotRequired[
        "aws_sdk_lakeformation.types.principal_resource_permissions_list.PrincipalResourcePermissionsList"
    ]
    """<p>A list of principals and their permissions on the resource for the specified principal and resource types.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPermissionsResponse) -> dict:
    out: dict = {}
    if "principal_resource_permissions" in value:
        import aws_sdk_lakeformation.types.principal_resource_permissions_list

        out["PrincipalResourcePermissions"] = (
            aws_sdk_lakeformation.types.principal_resource_permissions_list.serialize_json(
                value["principal_resource_permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListPermissionsResponse:
    out: ListPermissionsResponse = {}  # type: ignore[typeddict-item]
    if "PrincipalResourcePermissions" in data:
        import aws_sdk_lakeformation.types.principal_resource_permissions_list

        out["principal_resource_permissions"] = (
            aws_sdk_lakeformation.types.principal_resource_permissions_list.deserialize_json(
                data["PrincipalResourcePermissions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
