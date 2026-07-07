"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEksClusterResourcesVpcConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.boolean
    import aws_sdk_securityhub.types.non_empty_string_list


class AwsEksClusterResourcesVpcConfigDetails(TypedDict, closed=True):
    security_group_ids: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The security groups that are associated with the cross-account elastic network interfaces that are used to allow communication between your nodes and the Amazon EKS control plane.</p>"""
    subnet_ids: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string_list.NonEmptyStringList"
    ]
    """<p>The subnets that are associated with the cluster.</p>"""
    endpoint_public_access: NotRequired["aws_sdk_securityhub.types.boolean.Boolean"]
    """<p> Indicates whether the Amazon EKS public API server endpoint is turned on. If the Amazon EKS public API server endpoint is turned off, your cluster's Kubernetes API server can only receive requests that originate from within the cluster VPC. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksClusterResourcesVpcConfigDetails) -> dict:
    out: dict = {}
    if "security_group_ids" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["SecurityGroupIds"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["SubnetIds"] = (
            aws_sdk_securityhub.types.non_empty_string_list.serialize_json(
                value["subnet_ids"]
            )
        )
    if "endpoint_public_access" in value:
        out["EndpointPublicAccess"] = value["endpoint_public_access"]
    return out


def deserialize_json(data: dict) -> AwsEksClusterResourcesVpcConfigDetails:
    out: AwsEksClusterResourcesVpcConfigDetails = {}  # type: ignore[typeddict-item]
    if "SecurityGroupIds" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["security_group_ids"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["SecurityGroupIds"]
            )
        )
    if "SubnetIds" in data:
        import aws_sdk_securityhub.types.non_empty_string_list

        out["subnet_ids"] = (
            aws_sdk_securityhub.types.non_empty_string_list.deserialize_json(
                data["SubnetIds"]
            )
        )
    if "EndpointPublicAccess" in data:
        out["endpoint_public_access"] = data["EndpointPublicAccess"]
    return out
