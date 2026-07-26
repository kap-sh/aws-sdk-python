"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateVpcEndpointAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.subnet_mapping
    import capo_network_firewall.types.tag_list
    import capo_network_firewall.types.vpc_id


class CreateVpcEndpointAssociationRequest(TypedDict, closed=True):
    firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    vpc_id: "capo_network_firewall.types.vpc_id.VpcId"
    """<p>The unique identifier of the VPC where you want to create a firewall endpoint. </p>"""
    subnet_mapping: "capo_network_firewall.types.subnet_mapping.SubnetMapping"
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the VPC endpoint association. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVpcEndpointAssociationRequest) -> dict:
    out: dict = {}
    out["FirewallArn"] = value["firewall_arn"]
    out["VpcId"] = value["vpc_id"]
    import capo_network_firewall.types.subnet_mapping

    out["SubnetMapping"] = (
        capo_network_firewall.types.subnet_mapping.serialize_aws_json_1_0(
            value["subnet_mapping"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVpcEndpointAssociationRequest:
    out: CreateVpcEndpointAssociationRequest = {}  # type: ignore[typeddict-item]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        raise DeserializationError(
            "CreateVpcEndpointAssociationRequest.firewall_arn required"
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError(
            "CreateVpcEndpointAssociationRequest.vpc_id required"
        )
    if "SubnetMapping" in data:
        import capo_network_firewall.types.subnet_mapping

        out["subnet_mapping"] = (
            capo_network_firewall.types.subnet_mapping.deserialize_aws_json_1_0(
                data["SubnetMapping"]
            )
        )
    else:
        raise DeserializationError(
            "CreateVpcEndpointAssociationRequest.subnet_mapping required"
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
