"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkFabricConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_managedblockchain.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.edition


class NetworkFabricConfiguration(TypedDict, closed=True):
    edition: "aws_sdk_managedblockchain.types.edition.Edition"
    r"""<p>The edition of Amazon Managed Blockchain that the network uses. For more information, see <a href=\"http://aws.amazon.com/managed-blockchain/pricing/\">Amazon Managed Blockchain Pricing</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkFabricConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain.types.edition

    out["Edition"] = aws_sdk_managedblockchain.types.edition.serialize_json(
        value["edition"]
    )
    return out


def deserialize_json(data: dict) -> NetworkFabricConfiguration:
    out: NetworkFabricConfiguration = {}  # type: ignore[typeddict-item]
    if "Edition" in data:
        import aws_sdk_managedblockchain.types.edition

        out["edition"] = aws_sdk_managedblockchain.types.edition.deserialize_json(
            data["Edition"]
        )
    else:
        raise DeserializationError("NetworkFabricConfiguration.edition required")
    return out
