"""Generated from Smithy shape ``com.amazonaws.finspace#VpcConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_finspace.types.ip_address_type
    import capo_finspace.types.security_group_id_list
    import capo_finspace.types.subnet_id_list
    import capo_finspace.types.vpc_id_string


class VpcConfiguration(TypedDict, closed=True):
    vpc_id: NotRequired["capo_finspace.types.vpc_id_string.VpcIdString"]
    """<p>The identifier of the VPC endpoint.</p>"""
    security_group_ids: NotRequired[
        "capo_finspace.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The unique identifier of the VPC security group applied to the VPC endpoint ENI for the cluster.</p>"""
    subnet_ids: NotRequired["capo_finspace.types.subnet_id_list.SubnetIdList"]
    """<p>The identifier of the subnet that the Privatelink VPC endpoint uses to connect to the cluster.</p>"""
    ip_address_type: NotRequired["capo_finspace.types.ip_address_type.IPAddressType"]
    """<p>The IP address type for cluster network configuration parameters. The following type is available:</p> <ul> <li> <p>IP_V4 – IP address version 4</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: VpcConfiguration) -> dict:
    out: dict = {}
    if "vpc_id" in value:
        out["vpcId"] = value["vpc_id"]
    if "security_group_ids" in value:
        import capo_finspace.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_finspace.types.security_group_id_list.serialize_json(
                value["security_group_ids"]
            )
        )
    if "subnet_ids" in value:
        import capo_finspace.types.subnet_id_list

        out["subnetIds"] = capo_finspace.types.subnet_id_list.serialize_json(
            value["subnet_ids"]
        )
    if "ip_address_type" in value:
        import capo_finspace.types.ip_address_type

        out["ipAddressType"] = capo_finspace.types.ip_address_type.serialize_json(
            value["ip_address_type"]
        )
    return out


def deserialize_json(data: dict) -> VpcConfiguration:
    out: VpcConfiguration = {}  # type: ignore[typeddict-item]
    if "vpcId" in data:
        out["vpc_id"] = data["vpcId"]
    if "securityGroupIds" in data:
        import capo_finspace.types.security_group_id_list

        out["security_group_ids"] = (
            capo_finspace.types.security_group_id_list.deserialize_json(
                data["securityGroupIds"]
            )
        )
    if "subnetIds" in data:
        import capo_finspace.types.subnet_id_list

        out["subnet_ids"] = capo_finspace.types.subnet_id_list.deserialize_json(
            data["subnetIds"]
        )
    if "ipAddressType" in data:
        import capo_finspace.types.ip_address_type

        out["ip_address_type"] = capo_finspace.types.ip_address_type.deserialize_json(
            data["ipAddressType"]
        )
    return out
