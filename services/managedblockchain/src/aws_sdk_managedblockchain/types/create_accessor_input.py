"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateAccessorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.accessor_network_type
    import aws_sdk_managedblockchain.types.accessor_type
    import aws_sdk_managedblockchain.types.client_request_token_string
    import aws_sdk_managedblockchain.types.input_tag_map


class CreateAccessorInput(TypedDict, closed=True):
    client_request_token: "aws_sdk_managedblockchain.types.client_request_token_string.ClientRequestTokenString"
    """<p>This is a unique, case-sensitive identifier that you provide to ensure the idempotency of the operation. An idempotent operation completes no more than once. This identifier is required only if you make a service request directly using an HTTP client. It is generated automatically if you use an Amazon Web Services SDK or the Amazon Web Services CLI.</p>"""
    accessor_type: "aws_sdk_managedblockchain.types.accessor_type.AccessorType"
    """<p>The type of accessor.</p> <note> <p>Currently, accessor type is restricted to <code>BILLING_TOKEN</code>.</p> </note>"""
    tags: NotRequired["aws_sdk_managedblockchain.types.input_tag_map.InputTagMap"]
    r"""<p>Tags to assign to the Accessor.</p> <p> Each tag consists of a key and an optional value. You can specify multiple key-value pairs in a single request with an overall maximum of 50 tags allowed per resource.</p> <p>For more information about tags, see <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/ethereum-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Ethereum Developer Guide</i>, or <a href=\"https://docs.aws.amazon.com/managed-blockchain/latest/hyperledger-fabric-dev/tagging-resources.html\">Tagging Resources</a> in the <i>Amazon Managed Blockchain Hyperledger Fabric Developer Guide</i>.</p>"""
    network_type: NotRequired[
        "aws_sdk_managedblockchain.types.accessor_network_type.AccessorNetworkType"
    ]
    """<p>The blockchain network that the <code>Accessor</code> token is created for.</p> <note> <ul> <li> <p>Use the actual <code>networkType</code> value for the blockchain network that you are creating the <code>Accessor</code> token for.</p> </li> <li> <p>With the shut down of the <i>Ethereum Goerli</i> and <i>Polygon Mumbai Testnet</i> networks the following <code>networkType</code> values are no longer available for selection and use.</p> <ul> <li> <p> <code>ETHEREUM_MAINNET_AND_GOERLI</code> </p> </li> <li> <p> <code>ETHEREUM_GOERLI</code> </p> </li> <li> <p> <code>POLYGON_MUMBAI</code> </p> </li> </ul> <p>However, your existing <code>Accessor</code> tokens with these <code>networkType</code> values will remain unchanged.</p> </li> </ul> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAccessorInput) -> dict:
    out: dict = {}
    out["ClientRequestToken"] = value["client_request_token"]
    import aws_sdk_managedblockchain.types.accessor_type

    out["AccessorType"] = aws_sdk_managedblockchain.types.accessor_type.serialize_json(
        value["accessor_type"]
    )
    if "tags" in value:
        import aws_sdk_managedblockchain.types.input_tag_map

        out["Tags"] = aws_sdk_managedblockchain.types.input_tag_map.serialize_json(
            value["tags"]
        )
    if "network_type" in value:
        import aws_sdk_managedblockchain.types.accessor_network_type

        out["NetworkType"] = (
            aws_sdk_managedblockchain.types.accessor_network_type.serialize_json(
                value["network_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAccessorInput:
    out: CreateAccessorInput = {}  # type: ignore[typeddict-item]
    if "ClientRequestToken" in data:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        raise DeserializationError("CreateAccessorInput.client_request_token required")
    if "AccessorType" in data:
        import aws_sdk_managedblockchain.types.accessor_type

        out["accessor_type"] = (
            aws_sdk_managedblockchain.types.accessor_type.deserialize_json(
                data["AccessorType"]
            )
        )
    else:
        raise DeserializationError("CreateAccessorInput.accessor_type required")
    if "Tags" in data:
        import aws_sdk_managedblockchain.types.input_tag_map

        out["tags"] = aws_sdk_managedblockchain.types.input_tag_map.deserialize_json(
            data["Tags"]
        )
    if "NetworkType" in data:
        import aws_sdk_managedblockchain.types.accessor_network_type

        out["network_type"] = (
            aws_sdk_managedblockchain.types.accessor_network_type.deserialize_json(
                data["NetworkType"]
            )
        )
    return out
