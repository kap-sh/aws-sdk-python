"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdRoleMappingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.argo_cd_role_mapping

ArgoCdRoleMappingList: TypeAlias = list[
    "capo_eks.types.argo_cd_role_mapping.ArgoCdRoleMapping"
]


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdRoleMappingList) -> list:
    import capo_eks.types.argo_cd_role_mapping

    out: list = []
    for item in value:
        out.append(capo_eks.types.argo_cd_role_mapping.serialize_json(item))
    return out


def deserialize_json(data: list) -> ArgoCdRoleMappingList:
    import capo_eks.types.argo_cd_role_mapping

    out: ArgoCdRoleMappingList = []
    for item in data:
        out.append(capo_eks.types.argo_cd_role_mapping.deserialize_json(item))
    return out
