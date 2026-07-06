"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#AddressIdentifierFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_managedblockchain_query.types.chain_addresses


class AddressIdentifierFilter(TypedDict, closed=True):
    transaction_event_to_address: (
        "aws_sdk_managedblockchain_query.types.chain_addresses.ChainAddresses"
    )
    """<p>The container for the recipient address of the transaction. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AddressIdentifierFilter) -> dict:
    out: dict = {}
    import aws_sdk_managedblockchain_query.types.chain_addresses

    out["transactionEventToAddress"] = (
        aws_sdk_managedblockchain_query.types.chain_addresses.serialize_json(
            value["transaction_event_to_address"]
        )
    )
    return out


def deserialize_json(data: dict) -> AddressIdentifierFilter:
    out: AddressIdentifierFilter = {}  # type: ignore[typeddict-item]
    if "transactionEventToAddress" in data:
        import aws_sdk_managedblockchain_query.types.chain_addresses

        out["transaction_event_to_address"] = (
            aws_sdk_managedblockchain_query.types.chain_addresses.deserialize_json(
                data["transactionEventToAddress"]
            )
        )
    else:
        raise DeserializationError(
            "AddressIdentifierFilter.transaction_event_to_address required"
        )
    return out
