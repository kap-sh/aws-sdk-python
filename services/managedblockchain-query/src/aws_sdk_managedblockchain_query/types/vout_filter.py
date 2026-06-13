"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#VoutFilter``."""

from typing import TypedDict

from aws_sdk_managedblockchain_query.errors import DeserializationError


class VoutFilter(TypedDict):
    vout_spent: "bool"
    """<p>Specifies if the transaction output is spent or unspent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VoutFilter) -> dict:
    out: dict = {}
    out["voutSpent"] = value["vout_spent"]
    return out


def deserialize_json(data: dict) -> VoutFilter:
    out: VoutFilter = {}  # type: ignore[typeddict-item]
    if "voutSpent" in data:
        out["vout_spent"] = data["voutSpent"]
    else:
        raise DeserializationError("VoutFilter.vout_spent required")
    return out
