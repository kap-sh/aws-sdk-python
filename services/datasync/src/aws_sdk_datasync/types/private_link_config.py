"""Generated from Smithy shape ``com.amazonaws.datasync#PrivateLinkConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datasync.types.endpoint
    import aws_sdk_datasync.types.pl_security_group_arn_list
    import aws_sdk_datasync.types.pl_subnet_arn_list
    import aws_sdk_datasync.types.vpc_endpoint_id


class PrivateLinkConfig(TypedDict, closed=True):
    vpc_endpoint_id: NotRequired["aws_sdk_datasync.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>Specifies the ID of the VPC endpoint that your agent connects to.</p>"""
    private_link_endpoint: NotRequired["aws_sdk_datasync.types.endpoint.Endpoint"]
    r"""<p>Specifies the VPC endpoint provided by <a href=\"https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html\">Amazon Web Services PrivateLink</a> that your agent connects to.</p>"""
    subnet_arns: NotRequired[
        "aws_sdk_datasync.types.pl_subnet_arn_list.PLSubnetArnList"
    ]
    """<p>Specifies the ARN of the subnet where your VPC endpoint is located. You can only specify one ARN.</p>"""
    security_group_arns: NotRequired[
        "aws_sdk_datasync.types.pl_security_group_arn_list.PLSecurityGroupArnList"
    ]
    """<p>Specifies the Amazon Resource Names (ARN) of the security group that provides DataSync access to your VPC endpoint. You can only specify one ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrivateLinkConfig) -> dict:
    out: dict = {}
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "private_link_endpoint" in value:
        out["PrivateLinkEndpoint"] = value["private_link_endpoint"]
    if "subnet_arns" in value:
        import aws_sdk_datasync.types.pl_subnet_arn_list

        out["SubnetArns"] = (
            aws_sdk_datasync.types.pl_subnet_arn_list.serialize_aws_json_1_1(
                value["subnet_arns"]
            )
        )
    if "security_group_arns" in value:
        import aws_sdk_datasync.types.pl_security_group_arn_list

        out["SecurityGroupArns"] = (
            aws_sdk_datasync.types.pl_security_group_arn_list.serialize_aws_json_1_1(
                value["security_group_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PrivateLinkConfig:
    out: PrivateLinkConfig = {}  # type: ignore[typeddict-item]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if "PrivateLinkEndpoint" in data:
        out["private_link_endpoint"] = data["PrivateLinkEndpoint"]
    if "SubnetArns" in data:
        import aws_sdk_datasync.types.pl_subnet_arn_list

        out["subnet_arns"] = (
            aws_sdk_datasync.types.pl_subnet_arn_list.deserialize_aws_json_1_1(
                data["SubnetArns"]
            )
        )
    if "SecurityGroupArns" in data:
        import aws_sdk_datasync.types.pl_security_group_arn_list

        out["security_group_arns"] = (
            aws_sdk_datasync.types.pl_security_group_arn_list.deserialize_aws_json_1_1(
                data["SecurityGroupArns"]
            )
        )
    return out
