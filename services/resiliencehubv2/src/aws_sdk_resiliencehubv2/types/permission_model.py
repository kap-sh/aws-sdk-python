"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#PermissionModel``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.cross_account_role_list
    import aws_sdk_resiliencehubv2.types.iam_role_name


class PermissionModel(TypedDict):
    invoker_role_name: "aws_sdk_resiliencehubv2.types.iam_role_name.IamRoleName"
    cross_account_roles: NotRequired[
        "aws_sdk_resiliencehubv2.types.cross_account_role_list.CrossAccountRoleList"
    ]
    """<p>The list of cross-account IAM role ARNs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PermissionModel) -> dict:
    out: dict = {}
    out["invokerRoleName"] = value["invoker_role_name"]
    if "cross_account_roles" in value:
        import aws_sdk_resiliencehubv2.types.cross_account_role_list

        out["crossAccountRoles"] = (
            aws_sdk_resiliencehubv2.types.cross_account_role_list.serialize_json(
                value["cross_account_roles"]
            )
        )
    return out


def deserialize_json(data: dict) -> PermissionModel:
    out: PermissionModel = {}  # type: ignore[typeddict-item]
    if "invokerRoleName" in data:
        out["invoker_role_name"] = data["invokerRoleName"]
    else:
        raise DeserializationError("PermissionModel.invoker_role_name required")
    if "crossAccountRoles" in data:
        import aws_sdk_resiliencehubv2.types.cross_account_role_list

        out["cross_account_roles"] = (
            aws_sdk_resiliencehubv2.types.cross_account_role_list.deserialize_json(
                data["crossAccountRoles"]
            )
        )
    return out
