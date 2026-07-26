"""Generated from Smithy shape ``com.amazonaws.glue#PrincipalPermissions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.data_lake_principal
    import capo_glue.types.permission_list


class PrincipalPermissions(TypedDict, closed=True):
    principal: NotRequired["capo_glue.types.data_lake_principal.DataLakePrincipal"]
    """<p>The principal who is granted permissions.</p>"""
    permissions: NotRequired["capo_glue.types.permission_list.PermissionList"]
    """<p>The permissions that are granted to the principal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalPermissions) -> dict:
    out: dict = {}
    if "principal" in value:
        import capo_glue.types.data_lake_principal

        out["Principal"] = capo_glue.types.data_lake_principal.serialize_aws_json_1_1(
            value["principal"]
        )
    if "permissions" in value:
        import capo_glue.types.permission_list

        out["Permissions"] = capo_glue.types.permission_list.serialize_aws_json_1_1(
            value["permissions"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrincipalPermissions:
    out: PrincipalPermissions = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        import capo_glue.types.data_lake_principal

        out["principal"] = capo_glue.types.data_lake_principal.deserialize_aws_json_1_1(
            data["Principal"]
        )
    if "Permissions" in data:
        import capo_glue.types.permission_list

        out["permissions"] = capo_glue.types.permission_list.deserialize_aws_json_1_1(
            data["Permissions"]
        )
    return out
