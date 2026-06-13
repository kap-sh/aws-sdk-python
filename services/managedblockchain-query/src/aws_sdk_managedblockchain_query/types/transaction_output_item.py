"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TransactionOutputItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_managedblockchain_query.types.confirmation_status
    import aws_sdk_managedblockchain_query.types.query_network
    import aws_sdk_managedblockchain_query.types.query_transaction_hash
    import aws_sdk_managedblockchain_query.types.query_transaction_id


class TransactionOutputItem(TypedDict):
    transaction_hash: "aws_sdk_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash"
    """<p>The hash of a transaction. It is generated when a transaction is created.</p>"""
    transaction_id: NotRequired[
        "aws_sdk_managedblockchain_query.types.query_transaction_id.QueryTransactionId"
    ]
    """<p>The identifier of a Bitcoin transaction. It is generated when a transaction is created.</p>"""
    network: "aws_sdk_managedblockchain_query.types.query_network.QueryNetwork"
    """<p>The blockchain network where the transaction occurred.</p>"""
    transaction_timestamp: "datetime.datetime"
    """<p>The time when the transaction occurred.</p>"""
    confirmation_status: NotRequired[
        "aws_sdk_managedblockchain_query.types.confirmation_status.ConfirmationStatus"
    ]
    """<p>Specifies whether to list transactions that have not reached Finality.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransactionOutputItem) -> dict:
    out: dict = {}
    out["transactionHash"] = value["transaction_hash"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    out["network"] = value["network"]
    import aws_sdk_managedblockchain_query.types._prelude.timestamp

    out["transactionTimestamp"] = (
        aws_sdk_managedblockchain_query.types._prelude.timestamp.serialize_json(
            value["transaction_timestamp"]
        )
    )
    if "confirmation_status" in value:
        out["confirmationStatus"] = value["confirmation_status"]
    return out


def deserialize_json(data: dict) -> TransactionOutputItem:
    out: TransactionOutputItem = {}  # type: ignore[typeddict-item]
    if "transactionHash" in data:
        out["transaction_hash"] = data["transactionHash"]
    else:
        raise DeserializationError("TransactionOutputItem.transaction_hash required")
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    if "network" in data:
        out["network"] = data["network"]
    else:
        raise DeserializationError("TransactionOutputItem.network required")
    if "transactionTimestamp" in data:
        import aws_sdk_managedblockchain_query.types._prelude.timestamp

        out["transaction_timestamp"] = (
            aws_sdk_managedblockchain_query.types._prelude.timestamp.deserialize_json(
                data["transactionTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "TransactionOutputItem.transaction_timestamp required"
        )
    if "confirmationStatus" in data:
        out["confirmation_status"] = data["confirmationStatus"]
    return out
