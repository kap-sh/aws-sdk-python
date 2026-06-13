"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#TransactionEvent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.blockchain_instant
    import aws_sdk_managedblockchain_query.types.chain_address
    import aws_sdk_managedblockchain_query.types.confirmation_status
    import aws_sdk_managedblockchain_query.types.query_network
    import aws_sdk_managedblockchain_query.types.query_token_id
    import aws_sdk_managedblockchain_query.types.query_transaction_event_type
    import aws_sdk_managedblockchain_query.types.query_transaction_hash

TransactionEvent = TypedDict(
    "TransactionEvent",
    {
        "network": "aws_sdk_managedblockchain_query.types.query_network.QueryNetwork",
        "transaction_hash": "aws_sdk_managedblockchain_query.types.query_transaction_hash.QueryTransactionHash",
        "event_type": "aws_sdk_managedblockchain_query.types.query_transaction_event_type.QueryTransactionEventType",
        "from": NotRequired[
            "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "to": NotRequired[
            "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "value": NotRequired["str"],
        "contract_address": NotRequired[
            "aws_sdk_managedblockchain_query.types.chain_address.ChainAddress"
        ],
        "token_id": NotRequired[
            "aws_sdk_managedblockchain_query.types.query_token_id.QueryTokenId"
        ],
        "transaction_id": NotRequired["str"],
        "vout_index": NotRequired["int"],
        "vout_spent": NotRequired["bool"],
        "spent_vout_transaction_id": NotRequired["str"],
        "spent_vout_transaction_hash": NotRequired["str"],
        "spent_vout_index": NotRequired["int"],
        "blockchain_instant": NotRequired[
            "aws_sdk_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
        ],
        "confirmation_status": NotRequired[
            "aws_sdk_managedblockchain_query.types.confirmation_status.ConfirmationStatus"
        ],
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: TransactionEvent) -> dict:
    out: dict = {}
    out["network"] = value["network"]
    out["transactionHash"] = value["transaction_hash"]
    out["eventType"] = value["event_type"]
    if "from" in value:
        out["from"] = value["from"]
    if "to" in value:
        out["to"] = value["to"]
    if "value" in value:
        out["value"] = value["value"]
    if "contract_address" in value:
        out["contractAddress"] = value["contract_address"]
    if "token_id" in value:
        out["tokenId"] = value["token_id"]
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    if "vout_index" in value:
        out["voutIndex"] = value["vout_index"]
    if "vout_spent" in value:
        out["voutSpent"] = value["vout_spent"]
    if "spent_vout_transaction_id" in value:
        out["spentVoutTransactionId"] = value["spent_vout_transaction_id"]
    if "spent_vout_transaction_hash" in value:
        out["spentVoutTransactionHash"] = value["spent_vout_transaction_hash"]
    if "spent_vout_index" in value:
        out["spentVoutIndex"] = value["spent_vout_index"]
    if "blockchain_instant" in value:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["blockchainInstant"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["blockchain_instant"]
            )
        )
    if "confirmation_status" in value:
        out["confirmationStatus"] = value["confirmation_status"]
    return out


def deserialize_json(data: dict) -> TransactionEvent:
    out: TransactionEvent = {}  # type: ignore[typeddict-item]
    if "network" in data:
        out["network"] = data["network"]
    else:
        raise DeserializationError("TransactionEvent.network required")
    if "transactionHash" in data:
        out["transaction_hash"] = data["transactionHash"]
    else:
        raise DeserializationError("TransactionEvent.transaction_hash required")
    if "eventType" in data:
        out["event_type"] = data["eventType"]
    else:
        raise DeserializationError("TransactionEvent.event_type required")
    if "from" in data:
        out["from"] = data["from"]
    if "to" in data:
        out["to"] = data["to"]
    if "value" in data:
        out["value"] = data["value"]
    if "contractAddress" in data:
        out["contract_address"] = data["contractAddress"]
    if "tokenId" in data:
        out["token_id"] = data["tokenId"]
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    if "voutIndex" in data:
        out["vout_index"] = data["voutIndex"]
    if "voutSpent" in data:
        out["vout_spent"] = data["voutSpent"]
    if "spentVoutTransactionId" in data:
        out["spent_vout_transaction_id"] = data["spentVoutTransactionId"]
    if "spentVoutTransactionHash" in data:
        out["spent_vout_transaction_hash"] = data["spentVoutTransactionHash"]
    if "spentVoutIndex" in data:
        out["spent_vout_index"] = data["spentVoutIndex"]
    if "blockchainInstant" in data:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["blockchain_instant"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["blockchainInstant"]
            )
        )
    if "confirmationStatus" in data:
        out["confirmation_status"] = data["confirmationStatus"]
    return out
