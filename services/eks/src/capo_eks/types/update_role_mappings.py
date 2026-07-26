"""Generated from Smithy shape ``com.amazonaws.eks#UpdateRoleMappings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.argo_cd_role_mapping_list


class UpdateRoleMappings(TypedDict, closed=True):
    add_or_update_role_mappings: NotRequired[
        "capo_eks.types.argo_cd_role_mapping_list.ArgoCdRoleMappingList"
    ]
    """<p>A list of role mappings to add or update. If a mapping for the specified role already exists, it will be updated with the new identities. If it doesn't exist, a new mapping will be created.</p>"""
    remove_role_mappings: NotRequired[
        "capo_eks.types.argo_cd_role_mapping_list.ArgoCdRoleMappingList"
    ]
    """<p>A list of role mappings to remove from the RBAC configuration. Each mapping specifies an Argo CD role (<code>ADMIN</code>, <code>EDITOR</code>, or <code>VIEWER</code>) and the identities to remove from that role.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRoleMappings) -> dict:
    out: dict = {}
    if "add_or_update_role_mappings" in value:
        import capo_eks.types.argo_cd_role_mapping_list

        out["addOrUpdateRoleMappings"] = (
            capo_eks.types.argo_cd_role_mapping_list.serialize_json(
                value["add_or_update_role_mappings"]
            )
        )
    if "remove_role_mappings" in value:
        import capo_eks.types.argo_cd_role_mapping_list

        out["removeRoleMappings"] = (
            capo_eks.types.argo_cd_role_mapping_list.serialize_json(
                value["remove_role_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateRoleMappings:
    out: UpdateRoleMappings = {}  # type: ignore[typeddict-item]
    if "addOrUpdateRoleMappings" in data:
        import capo_eks.types.argo_cd_role_mapping_list

        out["add_or_update_role_mappings"] = (
            capo_eks.types.argo_cd_role_mapping_list.deserialize_json(
                data["addOrUpdateRoleMappings"]
            )
        )
    if "removeRoleMappings" in data:
        import capo_eks.types.argo_cd_role_mapping_list

        out["remove_role_mappings"] = (
            capo_eks.types.argo_cd_role_mapping_list.deserialize_json(
                data["removeRoleMappings"]
            )
        )
    return out
