"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#BatchGetTokenBalanceErrorItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_managedblockchain_query.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.blockchain_instant
    import aws_sdk_managedblockchain_query.types.error_type
    import aws_sdk_managedblockchain_query.types.owner_identifier
    import aws_sdk_managedblockchain_query.types.token_identifier

class BatchGetTokenBalanceErrorItem(TypedDict):
    token_identifier: NotRequired["aws_sdk_managedblockchain_query.types.token_identifier.TokenIdentifier"]
    owner_identifier: NotRequired["aws_sdk_managedblockchain_query.types.owner_identifier.OwnerIdentifier"]
    at_blockchain_instant: NotRequired["aws_sdk_managedblockchain_query.types.blockchain_instant.BlockchainInstant"]
    error_code: "str"
    """<p>The error code associated with the error.</p>"""
    error_message: "str"
    """<p>The message associated with the error.</p>"""
    error_type: "aws_sdk_managedblockchain_query.types.error_type.ErrorType"
    """<p>The type of error.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: BatchGetTokenBalanceErrorItem) -> dict:
    out: dict = {}
    if "token_identifier" in value:
        import aws_sdk_managedblockchain_query.types.token_identifier
        out["tokenIdentifier"] = aws_sdk_managedblockchain_query.types.token_identifier.serialize_json(value["token_identifier"])
    if "owner_identifier" in value:
        import aws_sdk_managedblockchain_query.types.owner_identifier
        out["ownerIdentifier"] = aws_sdk_managedblockchain_query.types.owner_identifier.serialize_json(value["owner_identifier"])
    if "at_blockchain_instant" in value:
        import aws_sdk_managedblockchain_query.types.blockchain_instant
        out["atBlockchainInstant"] = aws_sdk_managedblockchain_query.types.blockchain_instant.serialize_json(value["at_blockchain_instant"])
    out["errorCode"] = value["error_code"]
    out["errorMessage"] = value["error_message"]
    out["errorType"] = value["error_type"]
    return out


def deserialize_json(data: dict) -> BatchGetTokenBalanceErrorItem:
    out: BatchGetTokenBalanceErrorItem = {}  # type: ignore[typeddict-item]
    if "tokenIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.token_identifier
        out["token_identifier"] = aws_sdk_managedblockchain_query.types.token_identifier.deserialize_json(data["tokenIdentifier"])
    if "ownerIdentifier" in data:
        import aws_sdk_managedblockchain_query.types.owner_identifier
        out["owner_identifier"] = aws_sdk_managedblockchain_query.types.owner_identifier.deserialize_json(data["ownerIdentifier"])
    if "atBlockchainInstant" in data:
        import aws_sdk_managedblockchain_query.types.blockchain_instant
        out["at_blockchain_instant"] = aws_sdk_managedblockchain_query.types.blockchain_instant.deserialize_json(data["atBlockchainInstant"])
    if "errorCode" in data:
        out["error_code"] = data["errorCode"]
    else:
        raise DeserializationError("BatchGetTokenBalanceErrorItem.error_code required")
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    else:
        raise DeserializationError("BatchGetTokenBalanceErrorItem.error_message required")
    if "errorType" in data:
        out["error_type"] = data["errorType"]
    else:
        raise DeserializationError("BatchGetTokenBalanceErrorItem.error_type required")
    return out