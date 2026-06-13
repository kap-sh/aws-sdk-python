"""Generated from Smithy shape ``com.amazonaws.managedblockchainquery#ContractMetadata``."""

from typing import TypedDict

from typing_extensions import NotRequired


class ContractMetadata(TypedDict):
    name: NotRequired["str"]
    """<p>The name of the token contract.</p>"""
    symbol: NotRequired["str"]
    """<p>The symbol of the token contract.</p>"""
    decimals: NotRequired["int"]
    """<p>The decimals used by the token contract.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContractMetadata) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "symbol" in value:
        out["symbol"] = value["symbol"]
    if "decimals" in value:
        out["decimals"] = value["decimals"]
    return out


def deserialize_json(data: dict) -> ContractMetadata:
    out: ContractMetadata = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "symbol" in data:
        out["symbol"] = data["symbol"]
    if "decimals" in data:
        out["decimals"] = data["decimals"]
    return out
