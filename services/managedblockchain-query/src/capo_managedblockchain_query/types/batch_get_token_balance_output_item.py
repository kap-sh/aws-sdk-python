"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceOutputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.blockchain_instant
    import capo_managedblockchain_query.types.owner_identifier
    import capo_managedblockchain_query.types.token_identifier


class BatchGetTokenBalanceOutputItem(TypedDict, closed=True):
    owner_identifier: NotRequired[
        "capo_managedblockchain_query.types.owner_identifier.OwnerIdentifier"
    ]
    token_identifier: NotRequired[
        "capo_managedblockchain_query.types.token_identifier.TokenIdentifier"
    ]
    balance: "str"
    """<p>The container for the token balance.</p>"""
    at_blockchain_instant: (
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    )
    last_updated_time: NotRequired[
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceOutputItem) -> dict:
    out: dict = {}
    if "owner_identifier" in value:
        import capo_managedblockchain_query.types.owner_identifier

        out["ownerIdentifier"] = (
            capo_managedblockchain_query.types.owner_identifier.serialize_json(
                value["owner_identifier"]
            )
        )
    if "token_identifier" in value:
        import capo_managedblockchain_query.types.token_identifier

        out["tokenIdentifier"] = (
            capo_managedblockchain_query.types.token_identifier.serialize_json(
                value["token_identifier"]
            )
        )
    out["balance"] = value["balance"]
    import capo_managedblockchain_query.types.blockchain_instant

    out["atBlockchainInstant"] = (
        capo_managedblockchain_query.types.blockchain_instant.serialize_json(
            value["at_blockchain_instant"]
        )
    )
    if "last_updated_time" in value:
        import capo_managedblockchain_query.types.blockchain_instant

        out["lastUpdatedTime"] = (
            capo_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetTokenBalanceOutputItem:
    out: BatchGetTokenBalanceOutputItem = {}  # type: ignore[typeddict-item]
    if "ownerIdentifier" in data:
        import capo_managedblockchain_query.types.owner_identifier

        out["owner_identifier"] = (
            capo_managedblockchain_query.types.owner_identifier.deserialize_json(
                data["ownerIdentifier"]
            )
        )
    if "tokenIdentifier" in data:
        import capo_managedblockchain_query.types.token_identifier

        out["token_identifier"] = (
            capo_managedblockchain_query.types.token_identifier.deserialize_json(
                data["tokenIdentifier"]
            )
        )
    if "balance" in data:
        out["balance"] = data["balance"]
    else:
        raise DeserializationError("BatchGetTokenBalanceOutputItem.balance required")
    if "atBlockchainInstant" in data:
        import capo_managedblockchain_query.types.blockchain_instant

        out["at_blockchain_instant"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["atBlockchainInstant"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetTokenBalanceOutputItem.at_blockchain_instant required"
        )
    if "lastUpdatedTime" in data:
        import capo_managedblockchain_query.types.blockchain_instant

        out["last_updated_time"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    return out
