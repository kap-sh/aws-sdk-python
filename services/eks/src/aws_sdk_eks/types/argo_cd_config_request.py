"""Generated from Smithy shape ``com.amazonaws.eks#ArgoCdConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eks.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eks.types.argo_cd_aws_idc_config_request
    import aws_sdk_eks.types.argo_cd_network_access_config_request
    import aws_sdk_eks.types.argo_cd_role_mapping_list
    import aws_sdk_eks.types.string


class ArgoCdConfigRequest(TypedDict):
    namespace: NotRequired["aws_sdk_eks.types.string.String"]
    """<p>The Kubernetes namespace where Argo CD resources will be created. If not specified, the default namespace is used.</p>"""
    aws_idc: (
        "aws_sdk_eks.types.argo_cd_aws_idc_config_request.ArgoCdAwsIdcConfigRequest"
    )
    """<p>Configuration for IAM Identity CenterIAM; Identity Center integration. When configured, users can authenticate to Argo CD using their IAM Identity CenterIAM; Identity Center credentials.</p>"""
    rbac_role_mappings: NotRequired[
        "aws_sdk_eks.types.argo_cd_role_mapping_list.ArgoCdRoleMappingList"
    ]
    """<p>A list of role mappings that define which IAM Identity CenterIAM; Identity Center users or groups have which Argo CD roles. Each mapping associates an Argo CD role (<code>ADMIN</code>, <code>EDITOR</code>, or <code>VIEWER</code>) with one or more IAM Identity CenterIAM; Identity Center identities.</p>"""
    network_access: NotRequired[
        "aws_sdk_eks.types.argo_cd_network_access_config_request.ArgoCdNetworkAccessConfigRequest"
    ]
    """<p>Configuration for network access to the Argo CD capability's managed API server endpoint. By default, the Argo CD server is accessible via a public endpoint. You can optionally specify one or more VPC endpoint IDs to enable private connectivity from your VPCs. When VPC endpoints are configured, public access is blocked and the Argo CD server is only accessible through the specified VPC endpoints.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ArgoCdConfigRequest) -> dict:
    out: dict = {}
    if "namespace" in value:
        out["namespace"] = value["namespace"]
    import aws_sdk_eks.types.argo_cd_aws_idc_config_request

    out["awsIdc"] = aws_sdk_eks.types.argo_cd_aws_idc_config_request.serialize_json(
        value["aws_idc"]
    )
    if "rbac_role_mappings" in value:
        import aws_sdk_eks.types.argo_cd_role_mapping_list

        out["rbacRoleMappings"] = (
            aws_sdk_eks.types.argo_cd_role_mapping_list.serialize_json(
                value["rbac_role_mappings"]
            )
        )
    if "network_access" in value:
        import aws_sdk_eks.types.argo_cd_network_access_config_request

        out["networkAccess"] = (
            aws_sdk_eks.types.argo_cd_network_access_config_request.serialize_json(
                value["network_access"]
            )
        )
    return out


def deserialize_json(data: dict) -> ArgoCdConfigRequest:
    out: ArgoCdConfigRequest = {}  # type: ignore[typeddict-item]
    if "namespace" in data:
        out["namespace"] = data["namespace"]
    if "awsIdc" in data:
        import aws_sdk_eks.types.argo_cd_aws_idc_config_request

        out["aws_idc"] = (
            aws_sdk_eks.types.argo_cd_aws_idc_config_request.deserialize_json(
                data["awsIdc"]
            )
        )
    else:
        raise DeserializationError("ArgoCdConfigRequest.aws_idc required")
    if "rbacRoleMappings" in data:
        import aws_sdk_eks.types.argo_cd_role_mapping_list

        out["rbac_role_mappings"] = (
            aws_sdk_eks.types.argo_cd_role_mapping_list.deserialize_json(
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
