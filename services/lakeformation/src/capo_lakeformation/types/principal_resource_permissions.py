"""Generated from Smithy shape ``com.amazonaws.lakeformation#PrincipalResourcePermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.details_map
    import capo_lakeformation.types.last_modified_timestamp
    import capo_lakeformation.types.name_string
    import capo_lakeformation.types.permission_list
    import capo_lakeformation.types.resource


class PrincipalResourcePermissions(TypedDict, closed=True):
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>The Data Lake principal to be granted or revoked permissions.</p>"""
    resource: NotRequired["capo_lakeformation.types.resource.Resource"]
    """<p>The resource where permissions are to be granted or revoked.</p>"""
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    """<p>A Lake Formation condition, which applies to permissions and opt-ins that contain an expression.</p>"""
    permissions: NotRequired["capo_lakeformation.types.permission_list.PermissionList"]
    """<p>The permissions to be granted or revoked on the resource.</p>"""
    permissions_with_grant_option: NotRequired[
        "capo_lakeformation.types.permission_list.PermissionList"
    ]
    """<p>Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).</p>"""
    additional_details: NotRequired["capo_lakeformation.types.details_map.DetailsMap"]
    """<p>This attribute can be used to return any additional details of <code>PrincipalResourcePermissions</code>. Currently returns only as a RAM resource share ARN.</p>"""
    last_updated: NotRequired[
        "capo_lakeformation.types.last_modified_timestamp.LastModifiedTimestamp"
    ]
    """<p>The date and time when the resource was last updated.</p>"""
    last_updated_by: NotRequired["capo_lakeformation.types.name_string.NameString"]
    """<p>The user who updated the record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalResourcePermissions) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "resource" in value:
        import capo_lakeformation.types.resource

        out["Resource"] = capo_lakeformation.types.resource.serialize_json(
            value["resource"]
        )
    if "condition" in value:
        import capo_lakeformation.types.condition

        out["Condition"] = capo_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    if "permissions" in value:
        import capo_lakeformation.types.permission_list

        out["Permissions"] = capo_lakeformation.types.permission_list.serialize_json(
            value["permissions"]
        )
    if "permissions_with_grant_option" in value:
        import capo_lakeformation.types.permission_list

        out["PermissionsWithGrantOption"] = (
            capo_lakeformation.types.permission_list.serialize_json(
                value["permissions_with_grant_option"]
            )
        )
    if "additional_details" in value:
        import capo_lakeformation.types.details_map

        out["AdditionalDetails"] = capo_lakeformation.types.details_map.serialize_json(
            value["additional_details"]
        )
    if "last_updated" in value:
        import capo_lakeformation.types.last_modified_timestamp

        out["LastUpdated"] = (
            capo_lakeformation.types.last_modified_timestamp.serialize_json(
                value["last_updated"]
            )
        )
    if "last_updated_by" in value:
        out["LastUpdatedBy"] = value["last_updated_by"]
    return out


def deserialize_json(data: dict) -> PrincipalResourcePermissions:
    out: PrincipalResourcePermissions = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if "Resource" in data:
        import capo_lakeformation.types.resource

        out["resource"] = capo_lakeformation.types.resource.deserialize_json(
            data["Resource"]
        )
    if "Condition" in data:
        import capo_lakeformation.types.condition

        out["condition"] = capo_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    if "Permissions" in data:
        import capo_lakeformation.types.permission_list

        out["permissions"] = capo_lakeformation.types.permission_list.deserialize_json(
            data["Permissions"]
        )
    if "PermissionsWithGrantOption" in data:
        import capo_lakeformation.types.permission_list

        out["permissions_with_grant_option"] = (
            capo_lakeformation.types.permission_list.deserialize_json(
                data["PermissionsWithGrantOption"]
            )
        )
    if "AdditionalDetails" in data:
        import capo_lakeformation.types.details_map

        out["additional_details"] = (
            capo_lakeformation.types.details_map.deserialize_json(
                data["AdditionalDetails"]
            )
        )
    if "LastUpdated" in data:
        import capo_lakeformation.types.last_modified_timestamp

        out["last_updated"] = (
            capo_lakeformation.types.last_modified_timestamp.deserialize_json(
                data["LastUpdated"]
            )
        )
    if "LastUpdatedBy" in data:
        out["last_updated_by"] = data["LastUpdatedBy"]
    return out
