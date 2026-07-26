"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#OwnerIdentifier``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_managedblockchain_query.errors import DeserializationError

if TYPE_CHECKING:
    import capo_managedblockchain_query.types.chain_address


class OwnerIdentifier(TypedDict, closed=True):
    address: "capo_managedblockchain_query.types.chain_address.ChainAddress"
    """<p>The contract or wallet address for the owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OwnerIdentifier) -> dict:
    out: dict = {}
    out["address"] = value["address"]
    return out


def deserialize_json(data: dict) -> OwnerIdentifier:
    out: OwnerIdentifier = {}  # type: ignore[typeddict-item]
    if "address" in data:
        out["address"] = data["address"]
    else:
        raise DeserializationError("OwnerIdentifier.address required")
    return out
