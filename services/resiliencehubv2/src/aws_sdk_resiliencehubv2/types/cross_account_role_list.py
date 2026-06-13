"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#CrossAccountRoleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.cross_account_role

CrossAccountRoleList: TypeAlias = list[
    "aws_sdk_resiliencehubv2.types.cross_account_role.CrossAccountRole"
]


# --- restJson1 ser/de ---
def serialize_json(value: CrossAccountRoleList) -> list:
    import aws_sdk_resiliencehubv2.types.cross_account_role

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehubv2.types.cross_account_role.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CrossAccountRoleList:
    import aws_sdk_resiliencehubv2.types.cross_account_role

    out: CrossAccountRoleList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehubv2.types.cross_account_role.deserialize_json(item)
        )
    return out
