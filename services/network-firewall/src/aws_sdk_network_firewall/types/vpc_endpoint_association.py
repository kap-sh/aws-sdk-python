"""Generated from Smithy shape ``com.amazonaws.networkfirewall#VpcEndpointAssociation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.description
    import aws_sdk_network_firewall.types.resource_arn
    import aws_sdk_network_firewall.types.resource_id
    import aws_sdk_network_firewall.types.subnet_mapping
    import aws_sdk_network_firewall.types.tag_list
    import aws_sdk_network_firewall.types.vpc_id


class VpcEndpointAssociation(TypedDict):
    vpc_endpoint_association_id: NotRequired[
        "aws_sdk_network_firewall.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the VPC endpoint association. </p>"""
    vpc_endpoint_association_arn: (
        "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    )
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""
    firewall_arn: "aws_sdk_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    vpc_id: "aws_sdk_network_firewall.types.vpc_id.VpcId"
    """<p>The unique identifier of the VPC for the endpoint association. </p>"""
    subnet_mapping: "aws_sdk_network_firewall.types.subnet_mapping.SubnetMapping"
    description: NotRequired["aws_sdk_network_firewall.types.description.Description"]
    """<p>A description of the VPC endpoint association. </p>"""
    tags: NotRequired["aws_sdk_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: VpcEndpointAssociation) -> dict:
    out: dict = {}
    if "vpc_endpoint_association_id" in value:
        out["VpcEndpointAssociationId"] = value["vpc_endpoint_association_id"]
    out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    out["FirewallArn"] = value["firewall_arn"]
    out["VpcId"] = value["vpc_id"]
    import aws_sdk_network_firewall.types.subnet_mapping

    out["SubnetMapping"] = (
        aws_sdk_network_firewall.types.subnet_mapping.serialize_aws_json_1_0(
            value["subnet_mapping"]
        )
    )
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import aws_sdk_network_firewall.types.tag_list

        out["Tags"] = aws_sdk_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> VpcEndpointAssociation:
    out: VpcEndpointAssociation = {}  # type: ignore[typeddict-item]
    if "VpcEndpointAssociationId" in data:
        out["vpc_endpoint_association_id"] = data["VpcEndpointAssociationId"]
    if "VpcEndpointAssociationArn" in data:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    else:
        raise DeserializationError(
            "VpcEndpointAssociation.vpc_endpoint_association_arn required"
        )
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        raise DeserializationError("VpcEndpointAssociation.firewall_arn required")
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    else:
        raise DeserializationError("VpcEndpointAssociation.vpc_id required")
    if "SubnetMapping" in data:
        import aws_sdk_network_firewall.types.subnet_mapping

        out["subnet_mapping"] = (
            aws_sdk_network_firewall.types.subnet_mapping.deserialize_aws_json_1_0(
                data["SubnetMapping"]
            )
        )
    else:
        raise DeserializationError("VpcEndpointAssociation.subnet_mapping required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "Tags" in data:
        import aws_sdk_network_firewall.types.tag_list

        out["tags"] = aws_sdk_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
