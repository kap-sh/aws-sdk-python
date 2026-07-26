"""Generated from Smithy shape ``com.amazonaws.dax#SubnetGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.network_type_list
    import capo_dax.types.string
    import capo_dax.types.subnet_list


class SubnetGroup(TypedDict, closed=True):
    subnet_group_name: NotRequired["capo_dax.types.string.String"]
    """<p>The name of the subnet group.</p>"""
    description: NotRequired["capo_dax.types.string.String"]
    """<p>The description of the subnet group.</p>"""
    vpc_id: NotRequired["capo_dax.types.string.String"]
    """<p>The Amazon Virtual Private Cloud identifier (VPC ID) of the subnet group.</p>"""
    subnets: NotRequired["capo_dax.types.subnet_list.SubnetList"]
    """<p>A list of subnets associated with the subnet group. </p>"""
    supported_network_types: NotRequired[
        "capo_dax.types.network_type_list.NetworkTypeList"
    ]
    """<p>The network types supported by this subnet. Returns an array of strings that can include <code>ipv4</code>, <code>ipv6</code>, or both, indicating whether the subnet group supports IPv4 only, IPv6 only, or dual-stack deployments. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SubnetGroup) -> dict:
    out: dict = {}
    if "subnet_group_name" in value:
        out["SubnetGroupName"] = value["subnet_group_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "subnets" in value:
        import capo_dax.types.subnet_list

        out["Subnets"] = capo_dax.types.subnet_list.serialize_aws_json_1_1(
            value["subnets"]
        )
    if "supported_network_types" in value:
        import capo_dax.types.network_type_list

        out["SupportedNetworkTypes"] = (
            capo_dax.types.network_type_list.serialize_aws_json_1_1(
                value["supported_network_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SubnetGroup:
    out: SubnetGroup = {}  # type: ignore[typeddict-item]
    if "SubnetGroupName" in data:
        out["subnet_group_name"] = data["SubnetGroupName"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Subnets" in data:
        import capo_dax.types.subnet_list

        out["subnets"] = capo_dax.types.subnet_list.deserialize_aws_json_1_1(
            data["Subnets"]
        )
    if "SupportedNetworkTypes" in data:
        import capo_dax.types.network_type_list

        out["supported_network_types"] = (
            capo_dax.types.network_type_list.deserialize_aws_json_1_1(
                data["SupportedNetworkTypes"]
            )
        )
    return out
