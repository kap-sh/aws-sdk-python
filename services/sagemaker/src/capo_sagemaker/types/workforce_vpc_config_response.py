"""Generated from Smithy shape ``com.amazonaws.sagemaker#WorkforceVpcConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.workforce_security_group_ids
    import capo_sagemaker.types.workforce_subnets
    import capo_sagemaker.types.workforce_vpc_endpoint_id
    import capo_sagemaker.types.workforce_vpc_id


class WorkforceVpcConfigResponse(TypedDict, closed=True):
    vpc_id: NotRequired["capo_sagemaker.types.workforce_vpc_id.WorkforceVpcId"]
    """<p>The ID of the VPC that the workforce uses for communication.</p>"""
    security_group_ids: NotRequired[
        "capo_sagemaker.types.workforce_security_group_ids.WorkforceSecurityGroupIds"
    ]
    """<p>The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet.</p>"""
    subnets: NotRequired["capo_sagemaker.types.workforce_subnets.WorkforceSubnets"]
    """<p>The ID of the subnets in the VPC that you want to connect.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_sagemaker.types.workforce_vpc_endpoint_id.WorkforceVpcEndpointId"
    ]
    """<p>The IDs for the VPC service endpoints of your VPC workforce when it is created and updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkforceVpcConfigResponse) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "security_group_ids" in value:
        import capo_sagemaker.types.workforce_security_group_ids

        out["SecurityGroupIds"] = (
            capo_sagemaker.types.workforce_security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "subnets" in value:
        import capo_sagemaker.types.workforce_subnets

        out["Subnets"] = capo_sagemaker.types.workforce_subnets.serialize_aws_json_1_1(
            value["subnets"]
        )
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> WorkforceVpcConfigResponse:
    out: WorkforceVpcConfigResponse = {}  # type: ignore[typeddict-item]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SecurityGroupIds" in data:
        import capo_sagemaker.types.workforce_security_group_ids

        out["security_group_ids"] = (
            capo_sagemaker.types.workforce_security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "Subnets" in data:
        import capo_sagemaker.types.workforce_subnets

        out["subnets"] = (
            capo_sagemaker.types.workforce_subnets.deserialize_aws_json_1_1(
                data["Subnets"]
            )
        )
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
