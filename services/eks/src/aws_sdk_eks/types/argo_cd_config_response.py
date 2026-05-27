"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdConfigResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.argo_cd_aws_idc_config_response
    import aws_sdk_eks.types.argo_cd_network_access_config_response
    import aws_sdk_eks.types.argo_cd_role_mapping_list
    import aws_sdk_eks.types.string


class ArgoCdConfigResponse(TypedDict):
    namespace: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Kubernetes namespace where Argo CD resources are monitored by your Argo CD Capability.</p>"""
    aws_idc: NotRequired[
        "aws_sdk_eks.types.argo_cd_aws_idc_config_response.ArgoCdAwsIdcConfigResponse"
    ]
    """<p>The IAM Identity CenterIAM; Identity Center integration configuration.</p>"""
    rbac_role_mappings: NotRequired[
        "aws_sdk_eks.types.argo_cd_role_mapping_list.ArgoCdRoleMappingList"
    ]
    """<p>The list of role mappings that define which IAM Identity CenterIAM; Identity Center users or groups have which Argo CD roles.</p>"""
    network_access: NotRequired[
        "aws_sdk_eks.types.argo_cd_network_access_config_response.ArgoCdNetworkAccessConfigResponse"
    ]
    """<p>The network access configuration for the Argo CD capability's managed API server endpoint. If VPC endpoint IDs are specified, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.</p>"""
    server_url: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The URL of the Argo CD server. Use this URL to access the Argo CD web interface and API.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdConfigResponse) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    if "aws_idc" in value:
        import aws_sdk_eks.types.argo_cd_aws_idc_config_response

        out["awsIdc"] = (
            aws_sdk_eks.types.argo_cd_aws_idc_config_response.serialize_json(
                value["aws_idc"]
            )
        )
    if "rbac_role_mappings" in value:
        import aws_sdk_eks.types.argo_cd_role_mapping_list

        out["rbacRoleMappings"] = (
            aws_sdk_eks.types.argo_cd_role_mapping_list.serialize_json(
                value["rbac_role_mappings"]
            )
        )
    if "network_access" in value:
        import aws_sdk_eks.types.argo_cd_network_access_config_response

        out["networkAccess"] = (
            aws_sdk_eks.types.argo_cd_network_access_config_response.serialize_json(
                value["network_access"]
            )
        )
    if "server_url" in value:
        out["serverUrl"] = value["server_url"]
    return out


def deserialize_json(data: dict) -> ArgoCdConfigResponse:
    out: ArgoCdConfigResponse = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "awsIdc" in data:
        import aws_sdk_eks.types.argo_cd_aws_idc_config_response

        out["aws_idc"] = (
            aws_sdk_eks.types.argo_cd_aws_idc_config_response.deserialize_json(
                data["awsIdc"]
            )
        )
    if "rbacRoleMappings" in data:
        import aws_sdk_eks.types.argo_cd_role_mapping_list

        out["rbac_role_mappings"] = (
            aws_sdk_eks.types.argo_cd_role_mapping_list.deserialize_json(
                data["rbacRoleMappings"]
            )
        )
    if "networkAccess" in data:
        import aws_sdk_eks.types.argo_cd_network_access_config_response

        out["network_access"] = (
            aws_sdk_eks.types.argo_cd_network_access_config_response.deserialize_json(
                data["networkAccess"]
            )
        )
    if "serverUrl" in data:
        out["server_url"] = data["serverUrl"]
    return out
