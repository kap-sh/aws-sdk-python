"""Generated from Smithy shape ``com.amazonaws.lakeformation#PrincipalPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.data_lake_principal
    import capo_lakeformation.types.permission_list


class PrincipalPermissions(TypedDict, closed=True):
    principal: NotRequired[
        "capo_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>The principal who is granted permissions.</p>"""
    permissions: NotRequired["capo_lakeformation.types.permission_list.PermissionList"]
    """<p>The permissions that are granted to the principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalPermissions) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_lakeformation.types.data_lake_principal

        out["Principal"] = capo_lakeformation.types.data_lake_principal.serialize_json(
            value["principal"]
        )
    if "permissions" in value:
        import capo_lakeformation.types.permission_list

        out["Permissions"] = capo_lakeformation.types.permission_list.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> PrincipalPermissions:
    out: PrincipalPermissions = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        import capo_lakeformation.types.data_lake_principal

        out["principal"] = (
            capo_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if "Permissions" in data:
        import capo_lakeformation.types.permission_list

        out["permissions"] = capo_lakeformation.types.permission_list.deserialize_json(
            data["Permissions"]
        )
    return out
