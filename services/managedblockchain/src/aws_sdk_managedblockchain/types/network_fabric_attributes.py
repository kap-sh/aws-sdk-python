"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkFabricAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.edition
    import aws_sdk_managedblockchain.types.string


class NetworkFabricAttributes(TypedDict):
    ordering_service_endpoint: NotRequired[
        "aws_sdk_managedblockchain.types.string.String"
    ]
    """<p>The endpoint of the ordering service for the network.</p>"""
    edition: NotRequired["aws_sdk_managedblockchain.types.edition.Edition"]
    r"""<p>The edition of Amazon Managed Blockchain that Hyperledger Fabric uses. For more information, see <a href=\"http://aws.amazon.com/managed-blockchain/pricing/\">Amazon Managed Blockchain Pricing</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFabricAttributes) -> dict:
    out: dict = {}
    if "ordering_service_endpoint" in value:
        out["OrderingServiceEndpoint"] = value["ordering_service_endpoint"]
    if "edition" in value:
        import aws_sdk_managedblockchain.types.edition

        out["Edition"] = aws_sdk_managedblockchain.types.edition.serialize_json(
            value["edition"]
        )
    return out


def deserialize_json(data: dict) -> NetworkFabricAttributes:
    out: NetworkFabricAttributes = {}  # type: ignore[typeddict-item]
    if "OrderingServiceEndpoint" in data:
        out["ordering_service_endpoint"] = data["OrderingServiceEndpoint"]
    if "Edition" in data:
        import aws_sdk_managedblockchain.types.edition

        out["edition"] = aws_sdk_managedblockchain.types.edition.deserialize_json(
            data["Edition"]
        )
    return out
