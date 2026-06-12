"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceVpcConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.workforce_security_group_ids
    import aws_sdk_sagemaker.types.workforce_subnets
    import aws_sdk_sagemaker.types.workforce_vpc_id


class WorkforceVpcConfigRequest(TypedDict):
    vpc_id: NotRequired["aws_sdk_sagemaker.types.workforce_vpc_id.WorkforceVpcId"]
    """<p>The ID of the VPC that the workforce uses for communication.</p>"""
    security_group_ids: NotRequired[
        "aws_sdk_sagemaker.types.workforce_security_group_ids.WorkforceSecurityGroupIds"
    ]
    """<p>The VPC security group IDs, in the form <code>sg-xxxxxxxx</code>. The security groups must be for the same VPC as specified in the subnet.</p>"""
    subnets: NotRequired["aws_sdk_sagemaker.types.workforce_subnets.WorkforceSubnets"]
    """<p>The ID of the subnets in the VPC that you want to connect.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkforceVpcConfigRequest) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "security_group_ids" in value:
        import aws_sdk_sagemaker.types.workforce_security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_sagemaker.types.workforce_security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "subnets" in value:
        import aws_sdk_sagemaker.types.workforce_subnets

        out["Subnets"] = (
            aws_sdk_sagemaker.types.workforce_subnets.serialize_aws_json_1_1(
                value["subnets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkforceVpcConfigRequest:
    out: WorkforceVpcConfigRequest = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SecurityGroupIds" in data:
        import aws_sdk_sagemaker.types.workforce_security_group_ids

        out["security_group_ids"] = (
            aws_sdk_sagemaker.types.workforce_security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "Subnets" in data:
        import aws_sdk_sagemaker.types.workforce_subnets

        out["subnets"] = (
            aws_sdk_sagemaker.types.workforce_subnets.deserialize_aws_json_1_1(
                data["Subnets"]
            )
        )
    return out
