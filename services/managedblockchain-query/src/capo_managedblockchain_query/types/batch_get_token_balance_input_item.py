"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceInputItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.blockchain_instant
    import capo_managedblockchain_query.types.owner_identifier
    import capo_managedblockchain_query.types.token_identifier


class BatchGetTokenBalanceInputItem(TypedDict, closed=True):
    token_identifier: (
        "capo_managedblockchain_query.types.token_identifier.TokenIdentifier"
    )
    owner_identifier: (
        "capo_managedblockchain_query.types.owner_identifier.OwnerIdentifier"
    )
    at_blockchain_instant: NotRequired[
        "capo_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceInputItem) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.token_identifier

    out["tokenIdentifier"] = (
        capo_managedblockchain_query.types.token_identifier.serialize_json(
            value["token_identifier"]
        )
    )
    import capo_managedblockchain_query.types.owner_identifier

    out["ownerIdentifier"] = (
        capo_managedblockchain_query.types.owner_identifier.serialize_json(
            value["owner_identifier"]
        )
    )
    if "at_blockchain_instant" in value:
        import capo_managedblockchain_query.types.blockchain_instant

        out["atBlockchainInstant"] = (
            capo_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["at_blockchain_instant"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchGetTokenBalanceInputItem:
    out: BatchGetTokenBalanceInputItem = {}  # type: ignore[typeddict-item]
    if "tokenIdentifier" in data:
        import capo_managedblockchain_query.types.token_identifier

        out["token_identifier"] = (
            capo_managedblockchain_query.types.token_identifier.deserialize_json(
                data["tokenIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetTokenBalanceInputItem.token_identifier required"
        )
    if "ownerIdentifier" in data:
        import capo_managedblockchain_query.types.owner_identifier

        out["owner_identifier"] = (
            capo_managedblockchain_query.types.owner_identifier.deserialize_json(
                data["ownerIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "BatchGetTokenBalanceInputItem.owner_identifier required"
        )
    if "atBlockchainInstant" in data:
        import capo_managedblockchain_query.types.blockchain_instant

        out["at_blockchain_instant"] = (
            capo_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["atBlockchainInstant"]
            )
        )
    return out
