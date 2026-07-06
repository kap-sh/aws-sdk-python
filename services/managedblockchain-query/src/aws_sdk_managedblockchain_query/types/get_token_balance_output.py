"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetTokenBalanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.blockchain_instant
    import aws_sdk_managedblockchain_query.types.owner_identifier
    import aws_sdk_managedblockchain_query.types.token_identifier


class GetTokenBalanceOutput(TypedDict, closed=True):
    owner_identifier: NotRequired[
        "aws_sdk_managedblockchain_query.types.owner_identifier.OwnerIdentifier"
    ]
    token_identifier: NotRequired[
        "aws_sdk_managedblockchain_query.types.token_identifier.TokenIdentifier"
    ]
    balance: "str"
    """<p>The container for the token balance.</p>"""
    at_blockchain_instant: (
        "aws_sdk_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    )
    last_updated_time: NotRequired[
        "aws_sdk_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenBalanceOutput) -> dict:
    out: dict = {}
    if "owner_identifier" in value:
        import aws_sdk_managedblockchain_query.types.owner_identifier

        out["ownerIdentifier"] = (
            aws_sdk_managedblockchain_query.types.owner_identifier.serialize_json(
                value["owner_identifier"]
            )
        )
    if "token_identifier" in value:
        import aws_sdk_managedblockchain_query.types.token_identifier

        out["tokenIdentifier"] = (
            aws_sdk_managedblockchain_query.types.token_identifier.serialize_json(
                value["token_identifier"]
            )
        )
    out["balance"] = value["balance"]
    import aws_sdk_managedblockchain_query.types.blockchain_instant

    out["atBlockchainInstant"] = (
        aws_sdk_managedblockchain_query.types.blockchain_instant.serialize_json(
            value["at_blockchain_instant"]
        )
    )
    if "last_updated_time" in value:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["lastUpdatedTime"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["last_updated_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTokenBalanceOutput:
    out: GetTokenBalanceOutput = {}  # type: ignore[typeddict-item]
    if "ownerIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.owner_identifier

        out["owner_identifier"] = (
            aws_sdk_managedblockchain_query.types.owner_identifier.deserialize_json(
                data["ownerIdentifier"]
            )
        )
    if "tokenIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.token_identifier

        out["token_identifier"] = (
            aws_sdk_managedblockchain_query.types.token_identifier.deserialize_json(
                data["tokenIdentifier"]
            )
        )
    if "balance" in data:
        out["balance"] = data["balance"]
    else:
        raise DeserializationError("GetTokenBalanceOutput.balance required")
    if "atBlockchainInstant" in data:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["at_blockchain_instant"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["atBlockchainInstant"]
            )
        )
    else:
        raise DeserializationError(
            "GetTokenBalanceOutput.at_blockchain_instant required"
        )
    if "lastUpdatedTime" in data:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["last_updated_time"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["lastUpdatedTime"]
            )
        )
    return out
