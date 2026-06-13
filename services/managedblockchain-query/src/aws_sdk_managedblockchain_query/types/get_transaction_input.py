"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetTransactionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.query_network
    import aws_sdk_managedblockchain_query.types.query_transaction_hash
    import aws_sdk_managedblockchain_query.types.query_transaction_id


class GetTransactionInput(TypedDict):
    transaction_hash: NotRequired[
        "aws_sdk_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
    ]
    """<p>The hash of a transaction. It is generated when a transaction is created.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
    ]
    """<p>The identifier of a Bitcoin transaction. It is generated when a transaction is created.</p> <note> <p> <code>transactionId</code> is only supported on the Bitcoin networks.</p> </note>"""
    network: "aws_sdk_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network where the transaction occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransactionInput) -> dict:
    out: dict = {}
    if "transaction_hash" in value:
        out["transactionHash"] = value["transaction_hash"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    out["network"] = value["network"]
    return out


def deserialize_json(data: dict) -> GetTransactionInput:
    out: GetTransactionInput = {}  # type: ignore[typeddict-item]
    if "transactionHash" in data:
        out["transaction_hash"] = data["transactionHash"]
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    if "network" in data:
        out["network"] = data["network"]
    else:
        raise DeserializationError("GetTransactionInput.network required")
    return out
