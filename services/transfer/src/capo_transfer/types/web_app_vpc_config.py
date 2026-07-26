"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppVpcConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transfer.types.security_group_ids
    import capo_transfer.types.subnet_ids
    import capo_transfer.types.vpc_id
    import capo_transfer.types.web_app_vpc_endpoint_ip_address_type


class WebAppVpcConfig(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_transfer.types.subnet_ids.SubnetIds"]
    """<p>The list of subnet IDs within the VPC where the web app endpoint will be deployed. These subnets must be in the same VPC specified in the VpcId parameter.</p>"""
    vpc_id: NotRequired["capo_transfer.types.vpc_id.VpcId"]
    """<p>The identifier of the VPC where the web app endpoint will be hosted.</p>"""
    security_group_ids: NotRequired[
        "capo_transfer.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The list of security group IDs that control access to the web app endpoint. These security groups determine which sources can access the endpoint based on IP addresses and port configurations.</p>"""
    ip_address_type: NotRequired[
        "capo_transfer.types.web_app_vpc_endpoint_ip_address_type.WebAppVpcEndpointIpAddressType"
    ]
    """<p>The IP address type for the web app's VPC endpoint. This determines whether the endpoint is accessible over IPv4 only, or over both IPv4 and IPv6.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppVpcConfig) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_transfer.types.subnet_ids

        out["SubnetIds"] = capo_transfer.types.subnet_ids.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "security_group_ids" in value:
        import capo_transfer.types.security_group_ids

        out["SecurityGroupIds"] = (
            capo_transfer.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        import capo_transfer.types.web_app_vpc_endpoint_ip_address_type

        out["IpAddressType"] = (
            capo_transfer.types.web_app_vpc_endpoint_ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> WebAppVpcConfig:
    out: WebAppVpcConfig = {}  # type: ignore[typeddict-item]
    if "SubnetIds" in data:
        import capo_transfer.types.subnet_ids

        out["subnet_ids"] = capo_transfer.types.subnet_ids.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "SecurityGroupIds" in data:
        import capo_transfer.types.security_group_ids

        out["security_group_ids"] = (
            capo_transfer.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "IpAddressType" in data:
        import capo_transfer.types.web_app_vpc_endpoint_ip_address_type

        out["ip_address_type"] = (
            capo_transfer.types.web_app_vpc_endpoint_ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    return out
