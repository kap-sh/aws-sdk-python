"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateNodeInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.client_request_token_string
    import aws_sdk_managedblockchain.types.input_tag_map
    import aws_sdk_managedblockchain.types.node_configuration
    import aws_sdk_managedblockchain.types.resource_id_string


class CreateNodeInput(TypedDict):
    client_request_token: "aws_sdk_managedblockchain.types.client_request_token_string.ClientRequestTokenString"
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than one time. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the CLI.</p>"""
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network for the node.</p> <p>Ethereum public networks have the following <code>NetworkId</code>s:</p> <ul> <li> <p> <code>n-ethereum-mainnet</code> </p> </li> </ul>"""
    member_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier of the member that owns this node.</p> <p>Applies only to Hyperledger Fabric.</p>"""
    node_configuration: (
        "aws_sdk_managedblockchain.types.node_configuration.NodeConfiguration"
    )
    """<p>The properties of a node configuration.</p>"""
    tags: NotRequired["aws_sdk_managedblockchain.types.input_tag_map.InputTagMap"]
    r"""<p>Tags to assign to the node.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNodeInput) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    import aws_sdk_managedblockchain.types.node_configuration

    out["NodeConfiguration"] = (
        aws_sdk_managedblockchain.types.node_configuration.serialize_json(
            value["node_configuration"]
        )
    )
    if "tags" in value:
        import aws_sdk_managedblockchain.types.input_tag_map

        out["Tags"] = aws_sdk_managedblockchain.types.input_tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNodeInput:
    out: CreateNodeInput = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateNodeInput.client_request_token required")
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    if "NodeConfiguration" in data:
        import aws_sdk_managedblockchain.types.node_configuration

        out["node_configuration"] = (
            aws_sdk_managedblockchain.types.node_configuration.deserialize_json(
                data["NodeConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreateNodeInput.node_configuration required")
    if "Tags" in data:
        import aws_sdk_managedblockchain.types.input_tag_map

        out["tags"] = aws_sdk_managedblockchain.types.input_tag_map.deserialize_json(
            data["Tags"]
        )
    return out
