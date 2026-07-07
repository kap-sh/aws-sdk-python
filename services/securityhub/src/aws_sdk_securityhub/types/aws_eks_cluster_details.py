"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEksClusterDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_eks_cluster_logging_details
    import aws_sdk_securityhub.types.aws_eks_cluster_resources_vpc_config_details
    import aws_sdk_securityhub.types.non_empty_string


class AwsEksClusterDetails(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the cluster.</p>"""
    certificate_authority_data: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The certificate authority data for the cluster.</p>"""
    cluster_status: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The status of the cluster. Valid values are as follows:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATING</code> </p> </li> <li> <p> <code>DELETING</code> </p> </li> <li> <p> <code>FAILED</code> </p> </li> <li> <p> <code>PENDING</code> </p> </li> <li> <p> <code>UPDATING</code> </p> </li> </ul>"""
    endpoint: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The endpoint for the Amazon EKS API server.</p>"""
    name: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the cluster.</p>"""
    resources_vpc_config: NotRequired[
        "aws_sdk_securityhub.types.aws_eks_cluster_resources_vpc_config_details.AwsEksClusterResourcesVpcConfigDetails"
    ]
    """<p>The VPC configuration used by the cluster control plane.</p>"""
    role_arn: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the IAM role that provides permissions for the Amazon EKS control plane to make calls to Amazon Web Services API operations on your behalf.</p>"""
    version: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The Amazon EKS server version for the cluster.</p>"""
    logging: NotRequired[
        "aws_sdk_securityhub.types.aws_eks_cluster_logging_details.AwsEksClusterLoggingDetails"
    ]
    """<p>The logging configuration for the cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksClusterDetails) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "certificate_authority_data" in value:
        out["CertificateAuthorityData"] = value["certificate_authority_data"]
    if "cluster_status" in value:
        out["ClusterStatus"] = value["cluster_status"]
    if "endpoint" in value:
        out["Endpoint"] = value["endpoint"]
    if "name" in value:
        out["Name"] = value["name"]
    if "resources_vpc_config" in value:
        import aws_sdk_securityhub.types.aws_eks_cluster_resources_vpc_config_details

        out["ResourcesVpcConfig"] = (
            aws_sdk_securityhub.types.aws_eks_cluster_resources_vpc_config_details.serialize_json(
                value["resources_vpc_config"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "version" in value:
        out["Version"] = value["version"]
    if "logging" in value:
        import aws_sdk_securityhub.types.aws_eks_cluster_logging_details

        out["Logging"] = (
            aws_sdk_securityhub.types.aws_eks_cluster_logging_details.serialize_json(
                value["logging"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEksClusterDetails:
    out: AwsEksClusterDetails = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CertificateAuthorityData" in data:
        out["certificate_authority_data"] = data["CertificateAuthorityData"]
    if "ClusterStatus" in data:
        out["cluster_status"] = data["ClusterStatus"]
    if "Endpoint" in data:
        out["endpoint"] = data["Endpoint"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "ResourcesVpcConfig" in data:
        import aws_sdk_securityhub.types.aws_eks_cluster_resources_vpc_config_details

        out["resources_vpc_config"] = (
            aws_sdk_securityhub.types.aws_eks_cluster_resources_vpc_config_details.deserialize_json(
                data["ResourcesVpcConfig"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Logging" in data:
        import aws_sdk_securityhub.types.aws_eks_cluster_logging_details

        out["logging"] = (
            aws_sdk_securityhub.types.aws_eks_cluster_logging_details.deserialize_json(
                data["Logging"]
            )
        )
    return out
