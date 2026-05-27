"""Generated from Smithy shape ``com.amazonaws.eks#UpdateArgoCdConfig``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.argo_cd_network_access_config_request
    import aws_sdk_eks.types.update_role_mappings


class UpdateArgoCdConfig(TypedDict):
    rbac_role_mappings: NotRequired[
        "aws_sdk_eks.types.update_role_mappings.UpdateRoleMappings"
    ]
    """<p>Updated RBAC role mappings for the Argo CD capability. You can add, update, or remove role mappings.</p>"""
    network_access: NotRequired[
        "aws_sdk_eks.types.argo_cd_network_access_config_request.ArgoCdNetworkAccessConfigRequest"
    ]
    """<p>Updated network access configuration for the Argo CD capability's managed API server endpoint. You can add or remove VPC endpoint associations to control which VPCs have private access to the Argo CD server.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateArgoCdConfig) -> dict:
    out: dict = {}
    if "rbac_role_mappings" in value:
        import aws_sdk_eks.types.update_role_mappings

        out["rbacRoleMappings"] = aws_sdk_eks.types.update_role_mappings.serialize_json(
            value["rbac_role_mappings"]
        )
    if "network_access" in value:
        import aws_sdk_eks.types.argo_cd_network_access_config_request

        out["networkAccess"] = (
            aws_sdk_eks.types.argo_cd_network_access_config_request.serialize_json(
                value["network_access"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateArgoCdConfig:
    out: UpdateArgoCdConfig = {}  # type: ignore[typeddict-item]
    if "rbacRoleMappings" in data:
        import aws_sdk_eks.types.update_role_mappings

        out["rbac_role_mappings"] = (
            aws_sdk_eks.types.update_role_mappings.deserialize_json(
                data["rbacRoleMappings"]
            )
        )
    if "networkAccess" in data:
        import aws_sdk_eks.types.argo_cd_network_access_config_request

        out["network_access"] = (
            aws_sdk_eks.types.argo_cd_network_access_config_request.deserialize_json(
                data["networkAccess"]
            )
        )
    return out
