"""Generated from Smithy shape ``com.amazonaws.lakeformation#GrantPermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.condition
    import aws_sdk_lakeformation.types.data_lake_principal
    import aws_sdk_lakeformation.types.permission_list
    import aws_sdk_lakeformation.types.resource


class GrantPermissionsRequest(TypedDict, closed=True):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    principal: "aws_sdk_lakeformation.types.data_lake_principal.DataLakePrincipal"
    """<p>The principal to be granted the permissions on the resource. Supported principals are IAM users or IAM roles, and they are defined by their principal type and their ARN.</p> <p>Note that if you define a resource with a particular ARN, then later delete, and recreate a resource with that same ARN, the resource maintains the permissions already granted. </p>"""
    resource: "aws_sdk_lakeformation.types.resource.Resource"
    """<p>The resource to which permissions are to be granted. Resources in Lake Formation are the Data Catalog, databases, and tables.</p>"""
    permissions: "aws_sdk_lakeformation.types.permission_list.PermissionList"
    """<p>The permissions granted to the principal on the resource. Lake Formation defines privileges to grant and revoke access to metadata in the Data Catalog and data organized in underlying data storage such as Amazon S3. Lake Formation requires that each principal be authorized to perform a specific task on Lake Formation resources. </p>"""
    condition: NotRequired["aws_sdk_lakeformation.types.condition.Condition"]
    permissions_with_grant_option: NotRequired[
        "aws_sdk_lakeformation.types.permission_list.PermissionList"
    ]
    """<p>Indicates a list of the granted permissions that the principal may pass to other users. These permissions may only be a subset of the permissions granted in the <code>Privileges</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GrantPermissionsRequest) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    import aws_sdk_lakeformation.types.data_lake_principal

    out["Principal"] = aws_sdk_lakeformation.types.data_lake_principal.serialize_json(
        value["principal"]
    )
    import aws_sdk_lakeformation.types.resource

    out["Resource"] = aws_sdk_lakeformation.types.resource.serialize_json(
        value["resource"]
    )
    import aws_sdk_lakeformation.types.permission_list

    out["Permissions"] = aws_sdk_lakeformation.types.permission_list.serialize_json(
        value["permissions"]
    )
    if "condition" in value:
        import aws_sdk_lakeformation.types.condition

        out["Condition"] = aws_sdk_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    if "permissions_with_grant_option" in value:
        import aws_sdk_lakeformation.types.permission_list

        out["PermissionsWithGrantOption"] = (
            aws_sdk_lakeformation.types.permission_list.serialize_json(
                value["permissions_with_grant_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> GrantPermissionsRequest:
    out: GrantPermissionsRequest = {}  # type: ignore[typeddict-item]
    if "CatalogId" in data:
        out["catalog_id"] = data["CatalogId"]
    if "Principal" in data:
        import aws_sdk_lakeformation.types.data_lake_principal

        out["principal"] = (
            aws_sdk_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    else:
        raise DeserializationError("GrantPermissionsRequest.principal required")
    if "Resource" in data:
        import aws_sdk_lakeformation.types.resource

        out["resource"] = aws_sdk_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("GrantPermissionsRequest.resource required")
    if "Permissions" in data:
        import aws_sdk_lakeformation.types.permission_list

        out["permissions"] = (
            aws_sdk_lakeformation.types.permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError("GrantPermissionsRequest.permissions required")
    if "Condition" in data:
        import aws_sdk_lakeformation.types.condition

        out["condition"] = aws_sdk_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    if "PermissionsWithGrantOption" in data:
        import aws_sdk_lakeformation.types.permission_list

        out["permissions_with_grant_option"] = (
            aws_sdk_lakeformation.types.permission_list.deserialize_json(
                data["PermissionsWithGrantOption"]
            )
        )
    return out
