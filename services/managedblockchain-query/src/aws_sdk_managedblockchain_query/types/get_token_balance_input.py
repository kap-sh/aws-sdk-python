"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetTokenBalanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.blockchain_instant
    import aws_sdk_managedblockchain_query.types.owner_identifier
    import aws_sdk_managedblockchain_query.types.token_identifier


class GetTokenBalanceInput(TypedDict):
    token_identifier: (
        "aws_sdk_managedblockchain_query.types.token_identifier.TokenIdentifier"
    )
    """<p>The container for the identifier for the token, including the unique token ID and its blockchain network.</p>"""
    owner_identifier: (
        "aws_sdk_managedblockchain_query.types.owner_identifier.OwnerIdentifier"
    )
    """<p>The container for the identifier for the owner.</p>"""
    at_blockchain_instant: NotRequired[
        "aws_sdk_managedblockchain_query.types.blockchain_instant.BlockchainInstant"
    ]
    """<p>The time for when the TokenBalance is requested or the current time if a time is not provided in the request.</p> <note> <p>This time will only be recorded up to the second.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTokenBalanceInput) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.token_identifier

    out["tokenIdentifier"] = (
        aws_sdk_managedblockchain_query.types.token_identifier.serialize_json(
            value["token_identifier"]
        )
    )
    import aws_sdk_managedblockchain_query.types.owner_identifier

    out["ownerIdentifier"] = (
        aws_sdk_managedblockchain_query.types.owner_identifier.serialize_json(
            value["owner_identifier"]
        )
    )
    if "at_blockchain_instant" in value:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["atBlockchainInstant"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.serialize_json(
                value["at_blockchain_instant"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTokenBalanceInput:
    out: GetTokenBalanceInput = {}  # type: ignore[typeddict-item]
    if "tokenIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.token_identifier

        out["token_identifier"] = (
            aws_sdk_managedblockchain_query.types.token_identifier.deserialize_json(
                data["tokenIdentifier"]
            )
        )
    else:
        raise DeserializationError("GetTokenBalanceInput.token_identifier required")
    if "ownerIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.owner_identifier

        out["owner_identifier"] = (
            aws_sdk_managedblockchain_query.types.owner_identifier.deserialize_json(
                data["ownerIdentifier"]
            )
        )
    else:
        raise DeserializationError("GetTokenBalanceInput.owner_identifier required")
    if "atBlockchainInstant" in data:
        import aws_sdk_managedblockchain_query.types.blockchain_instant

        out["at_blockchain_instant"] = (
            aws_sdk_managedblockchain_query.types.blockchain_instant.deserialize_json(
                data["atBlockchainInstant"]
            )
        )
    return out
