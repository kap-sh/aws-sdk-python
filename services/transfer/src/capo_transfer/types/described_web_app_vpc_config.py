"""Generated from Smithy shape ``com.amazonaws.transfer#DescribedWebAppVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.subnet_ids
    import capo_transfer.types.vpc_endpoint_id
    import capo_transfer.types.vpc_id


class DescribedWebAppVpcConfig(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_transfer.types.subnet_ids.SubnetIds"]
    """<p>The list of subnet IDs within the VPC where the web app endpoint is deployed. These subnets must be in the same VPC and provide network connectivity for the endpoint.</p>"""
    vpc_id: NotRequired["capo_transfer.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC where the web app endpoint is hosted.</p>"""
    vpc_endpoint_id: NotRequired["capo_transfer.types.vpc_endpoint_id.VpcEndpointId"]
    """<p>The identifier of the VPC endpoint created for the web app.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribedWebAppVpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_transfer.types.subnet_ids

        out["SubnetIds"] = capo_transfer.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribedWebAppVpcConfig:
    out: DescribedWebAppVpcConfig = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import capo_transfer.types.subnet_ids

        out["subnet_ids"] = capo_transfer.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "VpcEndpointId" in data:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    return out
