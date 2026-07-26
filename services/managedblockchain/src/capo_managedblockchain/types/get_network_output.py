"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetNetworkOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_managedblockchain.types.network


class GetNetworkOutput(TypedDict, closed=True):
    network: NotRequired["capo_managedblockchain.types.network.Network"]
    """<p>An object containing network configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkOutput) -> dict:
    out: dict = {}
    if "network" in value:
        import capo_managedblockchain.types.network

        out["Network"] = capo_managedblockchain.types.network.serialize_json(
            value["network"]
        )
    return out


def deserialize_json(data: dict) -> GetNetworkOutput:
    out: GetNetworkOutput = {}  # type: ignore[typeddict-item]
    if "Network" in data:
        import capo_managedblockchain.types.network

        out["network"] = capo_managedblockchain.types.network.deserialize_json(
            data["Network"]
        )
    return out
