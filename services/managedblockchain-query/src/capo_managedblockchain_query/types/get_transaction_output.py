"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#GetTransactionOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.transaction


class GetTransactionOutput(TypedDict, closed=True):
    transaction: "capo_managedblockchain_query.types.transaction.Transaction"
    """<p>Contains the details of the transaction.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTransactionOutput) -> dict:
    out: dict = {}
    import capo_managedblockchain_query.types.transaction

    out["transaction"] = capo_managedblockchain_query.types.transaction.serialize_json(
        value["transaction"]
    )
    return out


def deserialize_json(data: dict) -> GetTransactionOutput:
    out: GetTransactionOutput = {}  # type: ignore[typeddict-item]
    if "transaction" in data:
        import capo_managedblockchain_query.types.transaction

        out["transaction"] = (
            capo_managedblockchain_query.types.transaction.deserialize_json(
                data["transaction"]
            )
        )
    else:
        raise DeserializationError("GetTransactionOutput.transaction required")
    return out
