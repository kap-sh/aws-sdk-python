"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetEffectivePermissionsForPathResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.principal_resource_permissions_list
    import aws_sdk_lakeformation.types.token


class GetEffectivePermissionsForPathResponse(TypedDict):
    permissions: NotRequired[
        "aws_sdk_lakeformation.types.principal_resource_permissions_list.PrincipalResourcePermissionsList"
    ]
    """<p>A list of the permissions for the specified table or database resource located at the path in Amazon S3.</p>"""
    next_token: NotRequired["aws_sdk_lakeformation.types.token.Token"]
    """<p>A continuation token, if this is not the first call to retrieve this list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEffectivePermissionsForPathResponse) -> dict:
    out: dict = {}
    if "permissions" in value:
        import aws_sdk_lakeformation.types.principal_resource_permissions_list

        out["Permissions"] = (
            aws_sdk_lakeformation.types.principal_resource_permissions_list.serialize_json(
                value["permissions"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetEffectivePermissionsForPathResponse:
    out: GetEffectivePermissionsForPathResponse = {}  # type: ignore[typeddict-item]
    if "Permissions" in data:
        import aws_sdk_lakeformation.types.principal_resource_permissions_list

        out["permissions"] = (
            aws_sdk_lakeformation.types.principal_resource_permissions_list.deserialize_json(
                data["Permissions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
