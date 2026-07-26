"""Generated from Smithy shape ``com.amazonaws.lakeformation#BatchPermissionsRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lakeformation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lakeformation.types.condition
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.identifier
    import capo_lakeformation.types.permission_list
    import capo_lakeformation.types.resource


class BatchPermissionsRequestEntry(TypedDict, closed=True):
    id: "capo_lakeformation.types.identifier.Identifier"
    """<p>A unique identifier for the batch permissions request entry.</p>"""
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>The principal to be granted a permission.</p>"""
    resource: NotRequired["capo_lakeformation.types.resource.Resource"]
    """<p>The resource to which the principal is to be granted a permission.</p>"""
    permissions: NotRequired["capo_lakeformation.types.permission_list.PermissionList"]
    """<p>The permissions to be granted.</p>"""
    condition: NotRequired["capo_lakeformation.types.condition.Condition"]
    permissions_with_grant_option: NotRequired[
        "capo_lakeformation.types.permission_list.PermissionList"
    ]
    """<p>Indicates if the option to pass permissions is granted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPermissionsRequestEntry) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
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
    if "permissions" in value:
        import capo_lakeformation.types.permission_list

        out["Permissions"] = capo_lakeformation.types.permission_list.serialize_json(
            value["permissions"]
        )
    if "condition" in value:
        import capo_lakeformation.types.condition

        out["Condition"] = capo_lakeformation.types.condition.serialize_json(
            value["condition"]
        )
    if "permissions_with_grant_option" in value:
        import capo_lakeformation.types.permission_list

        out["PermissionsWithGrantOption"] = (
            capo_lakeformation.types.permission_list.serialize_json(
                value["permissions_with_grant_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchPermissionsRequestEntry:
    out: BatchPermissionsRequestEntry = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("BatchPermissionsRequestEntry.id required")
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
    if "Permissions" in data:
        import capo_lakeformation.types.permission_list

        out["permissions"] = capo_lakeformation.types.permission_list.deserialize_json(
            data["Permissions"]
        )
    if "Condition" in data:
        import capo_lakeformation.types.condition

        out["condition"] = capo_lakeformation.types.condition.deserialize_json(
            data["Condition"]
        )
    if "PermissionsWithGrantOption" in data:
        import capo_lakeformation.types.permission_list

        out["permissions_with_grant_option"] = (
            capo_lakeformation.types.permission_list.deserialize_json(
                data["PermissionsWithGrantOption"]
            )
        )
    return out
