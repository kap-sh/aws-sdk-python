"""Generated from Smithy shape ``com.amazonaws.pcs#NetworkingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.network_type
    import capo_pcs.types.security_group_id_list
    import capo_pcs.types.subnet_id_list


class NetworkingRequest(TypedDict, closed=True):
    subnet_ids: NotRequired["capo_pcs.types.subnet_id_list.SubnetIdList"]
    """<p>The list of subnet IDs where PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and PCS resources. Subnet IDs have the form <code>subnet-0123456789abcdef0</code>.</p> <p>Subnets can't be in Outposts, Wavelength or an Amazon Web Services Local Zone.</p> <note> <p>PCS currently supports only 1 subnet in this list.</p> </note>"""
    security_group_ids: NotRequired[
        "capo_pcs.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>A list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.</p>"""
    network_type: NotRequired["capo_pcs.types.network_type.NetworkType"]
    """<p>The IP address version the cluster uses. The default is <code>IPV4</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkingRequest) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import capo_pcs.types.subnet_id_list

        out["subnetIds"] = capo_pcs.types.subnet_id_list.serialize_aws_json_1_0(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import capo_pcs.types.security_group_id_list

        out["securityGroupIds"] = (
            capo_pcs.types.security_group_id_list.serialize_aws_json_1_0(
                value["security_group_ids"]
            )
        )
    if "network_type" in value:
        import capo_pcs.types.network_type

        out["networkType"] = capo_pcs.types.network_type.serialize_aws_json_1_0(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> NetworkingRequest:
    out: NetworkingRequest = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import capo_pcs.types.subnet_id_list

        out["subnet_ids"] = capo_pcs.types.subnet_id_list.deserialize_aws_json_1_0(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import capo_pcs.types.security_group_id_list

        out["security_group_ids"] = (
            capo_pcs.types.security_group_id_list.deserialize_aws_json_1_0(
                data["securityGroupIds"]
            )
        )
    if "networkType" in data:
        import capo_pcs.types.network_type

        out["network_type"] = capo_pcs.types.network_type.deserialize_aws_json_1_0(
            data["networkType"]
        )
    return out
