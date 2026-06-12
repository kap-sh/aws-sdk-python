"""Generated from Smithy shape ``com.amazonaws.lakeformation#RevokePermissionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.catalog_id_string
    import aws_sdk_lakeformation.types.condition
    import aws_sdk_lakeformation.types.data_lake_principal
    import aws_sdk_lakeformation.types.permission_list
    import aws_sdk_lakeformation.types.resource


class RevokePermissionsRequest(TypedDict):
    catalog_id: NotRequired[
        "aws_sdk_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment. </p>"""
    principal: "aws_sdk_lakeformation.types.data_lake_principal.DataLakePrincipal"
    """<p>The principal to be revoked permissions on the resource.</p>"""
    resource: "aws_sdk_lakeformation.types.resource.Resource"
    """<p>The resource to which permissions are to be revoked.</p>"""
    permissions: "aws_sdk_lakeformation.types.permission_list.PermissionList"
    """<p>The permissions revoked to the principal on the resource. For information about permissions, see <a href=\"https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html\">Security and Access Control to Metadata and Data</a>.</p>"""
    condition: NotRequired["aws_sdk_lakeformation.types.condition.Condition"]
    permissions_with_grant_option: NotRequired[
        "aws_sdk_lakeformation.types.permission_list.PermissionList"
    ]
    """<p>Indicates a list of permissions for which to revoke the grant option allowing the principal to pass permissions to other principals.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevokePermissionsRequest) -> dict:
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


def deserialize_json(data: dict) -> RevokePermissionsRequest:
    out: RevokePermissionsRequest = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("RevokePermissionsRequest.principal required")
    if "Resource" in data:
        import aws_sdk_lakeformation.types.resource

        out["resource"] = aws_sdk_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    else:
        raise DeserializationError("RevokePermissionsRequest.resource required")
    if "Permissions" in data:
        import aws_sdk_lakeformation.types.permission_list

        out["permissions"] = (
            aws_sdk_lakeformation.types.permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    else:
        raise DeserializationError("RevokePermissionsRequest.permissions required")
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
