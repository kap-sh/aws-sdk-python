"""Generated from Smithy shape ``com.amazonaws.lakeformation#PrincipalPermissions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lakeformation.types.data_lake_principal
    import aws_sdk_lakeformation.types.permission_list


class PrincipalPermissions(TypedDict):
    principal: NotRequired[
        "aws_sdk_lakeformation.types.data_lake_principal.DataLakePrincipal"
    ]
    """<p>The principal who is granted permissions.</p>"""
    permissions: NotRequired[
        "aws_sdk_lakeformation.types.permission_list.PermissionList"
    ]
    """<p>The permissions that are granted to the principal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalPermissions) -> dict:
    out: dict = {}
    if "principal" in value:
        import aws_sdk_lakeformation.types.data_lake_principal

        out["Principal"] = (
            aws_sdk_lakeformation.types.data_lake_principal.serialize_json(
                value["principal"]
            )
        )
    if "permissions" in value:
        import aws_sdk_lakeformation.types.permission_list

        out["Permissions"] = aws_sdk_lakeformation.types.permission_list.serialize_json(
            value["permissions"]
        )
    return out


def deserialize_json(data: dict) -> PrincipalPermissions:
    out: PrincipalPermissions = {}  # type: ignore[typeddict-item]
    if "Principal" in data:
        import aws_sdk_lakeformation.types.data_lake_principal

        out["principal"] = (
            aws_sdk_lakeformation.types.data_lake_principal.deserialize_json(
                data["Principal"]
            )
        )
    if "Permissions" in data:
        import aws_sdk_lakeformation.types.permission_list

        out["permissions"] = (
            aws_sdk_lakeformation.types.permission_list.deserialize_json(
                data["Permissions"]
            )
        )
    return out
