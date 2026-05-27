"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdRoleMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.argo_cd_role_mapping

ArgoCdRoleMappingList: TypeAlias = list[
    "aws_sdk_eks.types.argo_cd_role_mapping.ArgoCdRoleMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdRoleMappingList) -> list:
    import aws_sdk_eks.types.argo_cd_role_mapping

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.argo_cd_role_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArgoCdRoleMappingList:
    import aws_sdk_eks.types.argo_cd_role_mapping

    out: ArgoCdRoleMappingList = []
    for item in data:
        out.append(aws_sdk_eks.types.argo_cd_role_mapping.deserialize_json(item))
    return out
