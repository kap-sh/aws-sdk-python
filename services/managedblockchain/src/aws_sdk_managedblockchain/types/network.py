"""Generated from Smithy shape ``com.amazonaws.managedblockchain#Network``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.arn_string
    import aws_sdk_managedblockchain.types.description_string
    import aws_sdk_managedblockchain.types.framework
    import aws_sdk_managedblockchain.types.framework_version_string
    import aws_sdk_managedblockchain.types.name_string
    import aws_sdk_managedblockchain.types.network_framework_attributes
    import aws_sdk_managedblockchain.types.network_status
    import aws_sdk_managedblockchain.types.output_tag_map
    import aws_sdk_managedblockchain.types.resource_id_string
    import aws_sdk_managedblockchain.types.string
    import aws_sdk_managedblockchain.types.timestamp
    import aws_sdk_managedblockchain.types.voting_policy


class Network(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the network.</p>"""
    name: NotRequired["aws_sdk_managedblockchain.types.name_string.NameString"]
    """<p>The name of the network.</p>"""
    description: NotRequired[
        "aws_sdk_managedblockchain.types.description_string.DescriptionString"
    ]
    """<p>Attributes of the blockchain framework for the network.</p>"""
    framework: NotRequired["aws_sdk_managedblockchain.types.framework.Framework"]
    """<p>The blockchain framework that the network uses.</p>"""
    framework_version: NotRequired[
        "aws_sdk_managedblockchain.types.framework_version_string.FrameworkVersionString"
    ]
    """<p>The version of the blockchain framework that the network uses.</p>"""
    framework_attributes: NotRequired[
        "aws_sdk_managedblockchain.types.network_framework_attributes.NetworkFrameworkAttributes"
    ]
    """<p>Attributes of the blockchain framework that the network uses.</p>"""
    vpc_endpoint_service_name: NotRequired[
        "aws_sdk_managedblockchain.types.string.String"
    ]
    """<p>The VPC endpoint service name of the VPC endpoint service of the network. Members use the VPC endpoint service name to create a VPC endpoint to access network resources.</p>"""
    voting_policy: NotRequired[
        "aws_sdk_managedblockchain.types.voting_policy.VotingPolicy"
    ]
    """<p>The voting rules that the network uses to decide if a proposal is accepted.</p>"""
    status: NotRequired["aws_sdk_managedblockchain.types.network_status.NetworkStatus"]
    """<p>The current status of the network.</p>"""
    creation_date: NotRequired["aws_sdk_managedblockchain.types.timestamp.Timestamp"]
    """<p>The date and time that the network was created.</p>"""
    tags: NotRequired["aws_sdk_managedblockchain.types.output_tag_map.OutputTagMap"]
    r"""<p>Tags assigned to the network. Each tag consists of a key and optional value.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""
    arn: NotRequired["aws_sdk_managedblockchain.types.arn_string.ArnString"]
    r"""<p>The Amazon Resource Name (ARN) of the network. For more information about ARNs and their format, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\">Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Network) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "framework" in value:
        import aws_sdk_managedblockchain.types.framework

        out["Framework"] = aws_sdk_managedblockchain.types.framework.serialize_json(
            value["framework"]
        )
    if "framework_version" in value:
        out["FrameworkVersion"] = value["framework_version"]
    if "framework_attributes" in value:
        import aws_sdk_managedblockchain.types.network_framework_attributes

        out["FrameworkAttributes"] = (
            aws_sdk_managedblockchain.types.network_framework_attributes.serialize_json(
                value["framework_attributes"]
            )
        )
    if "vpc_endpoint_service_name" in value:
        out["VpcEndpointServiceName"] = value["vpc_endpoint_service_name"]
    if "voting_policy" in value:
        import aws_sdk_managedblockchain.types.voting_policy

        out["VotingPolicy"] = (
            aws_sdk_managedblockchain.types.voting_policy.serialize_json(
                value["voting_policy"]
            )
        )
    if "status" in value:
        import aws_sdk_managedblockchain.types.network_status

        out["Status"] = aws_sdk_managedblockchain.types.network_status.serialize_json(
            value["status"]
        )
    if "creation_date" in value:
        import aws_sdk_managedblockchain.types.timestamp

        out["CreationDate"] = aws_sdk_managedblockchain.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "tags" in value:
        import aws_sdk_managedblockchain.types.output_tag_map

        out["Tags"] = aws_sdk_managedblockchain.types.output_tag_map.serialize_json(
            value["tags"]
        )
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> Network:
    out: Network = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Framework" in data:
        import aws_sdk_managedblockchain.types.framework

        out["framework"] = aws_sdk_managedblockchain.types.framework.deserialize_json(
            data["Framework"]
        )
    if "FrameworkVersion" in data:
        out["framework_version"] = data["FrameworkVersion"]
    if "FrameworkAttributes" in data:
        import aws_sdk_managedblockchain.types.network_framework_attributes

        out["framework_attributes"] = (
            aws_sdk_managedblockchain.types.network_framework_attributes.deserialize_json(
                data["FrameworkAttributes"]
            )
        )
    if "VpcEndpointServiceName" in data:
        out["vpc_endpoint_service_name"] = data["VpcEndpointServiceName"]
    if "VotingPolicy" in data:
        import aws_sdk_managedblockchain.types.voting_policy

        out["voting_policy"] = (
            aws_sdk_managedblockchain.types.voting_policy.deserialize_json(
                data["VotingPolicy"]
            )
        )
    if "Status" in data:
        import aws_sdk_managedblockchain.types.network_status

        out["status"] = aws_sdk_managedblockchain.types.network_status.deserialize_json(
            data["Status"]
        )
    if "CreationDate" in data:
        import aws_sdk_managedblockchain.types.timestamp

        out["creation_date"] = (
            aws_sdk_managedblockchain.types.timestamp.deserialize_json(
                data["CreationDate"]
            )
        )
    if "Tags" in data:
        import aws_sdk_managedblockchain.types.output_tag_map

        out["tags"] = aws_sdk_managedblockchain.types.output_tag_map.deserialize_json(
            data["Tags"]
        )
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
