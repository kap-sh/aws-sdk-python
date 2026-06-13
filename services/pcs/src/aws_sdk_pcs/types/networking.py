"""Generated from Smithy shape ``com.amazonaws.pcs#Networking``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pcs.types.network_type
    import aws_sdk_pcs.types.security_group_id_list
    import aws_sdk_pcs.types.subnet_id_list


class Networking(TypedDict):
    subnet_ids: NotRequired["aws_sdk_pcs.types.subnet_id_list.SubnetIdList"]
    """<p>The ID of the subnet where PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and PCS resources. The subnet must have an available IP address, cannot reside in Outposts, Wavelength, or an Amazon Web Services Local Zone.</p> <p> Example: <code>subnet-abcd1234</code> </p>"""
    security_group_ids: NotRequired[
        "aws_sdk_pcs.types.security_group_id_list.SecurityGroupIdList"
    ]
    """<p>The list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.</p> <p>The following rules are required:</p> <ul> <li> <p>Inbound rule 1</p> <ul> <li> <p>Protocol: All</p> </li> <li> <p>Ports: All</p> </li> <li> <p>Source: Self</p> </li> </ul> </li> <li> <p>Outbound rule 1</p> <ul> <li> <p>Protocol: All</p> </li> <li> <p>Ports: All</p> </li> <li> <p>Destination: 0.0.0.0/0 (IPv4) or ::/0 (IPv6)</p> </li> </ul> </li> <li> <p>Outbound rule 2</p> <ul> <li> <p>Protocol: All</p> </li> <li> <p>Ports: All</p> </li> <li> <p>Destination: Self</p> </li> </ul> </li> </ul>"""
    network_type: NotRequired["aws_sdk_pcs.types.network_type.NetworkType"]
    """<p>The IP address version the cluster uses. The default is <code>IPV4</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Networking) -> dict:
    out: dict = {}
    if "subnet_ids" in value:
        import aws_sdk_pcs.types.subnet_id_list

        out["subnetIds"] = aws_sdk_pcs.types.subnet_id_list.serialize_aws_json_1_0(
            value["subnet_ids"]
        )
    if "security_group_ids" in value:
        import aws_sdk_pcs.types.security_group_id_list

        out["securityGroupIds"] = (
            aws_sdk_pcs.types.security_group_id_list.serialize_aws_json_1_0(
                value["security_group_ids"]
            )
        )
    if "network_type" in value:
        import aws_sdk_pcs.types.network_type

        out["networkType"] = aws_sdk_pcs.types.network_type.serialize_aws_json_1_0(
            value["network_type"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Networking:
    out: Networking = {}  # type: ignore[typeddict-item]
    if "subnetIds" in data:
        import aws_sdk_pcs.types.subnet_id_list

        out["subnet_ids"] = aws_sdk_pcs.types.subnet_id_list.deserialize_aws_json_1_0(
            data["subnetIds"]
        )
    if "securityGroupIds" in data:
        import aws_sdk_pcs.types.security_group_id_list

        out["security_group_ids"] = (
            aws_sdk_pcs.types.security_group_id_list.deserialize_aws_json_1_0(
                data["securityGroupIds"]
            )
        )
    if "networkType" in data:
        import aws_sdk_pcs.types.network_type

        out["network_type"] = aws_sdk_pcs.types.network_type.deserialize_aws_json_1_0(
            data["networkType"]
        )
    return out
