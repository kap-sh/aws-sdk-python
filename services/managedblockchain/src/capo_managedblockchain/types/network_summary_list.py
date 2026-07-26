"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_managedblockchain.types.network_summary

NetworkSummaryList: TypeAlias = list[
    "capo_managedblockchain.types.network_summary.NetworkSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSummaryList) -> list:
    import capo_managedblockchain.types.network_summary

    out: list = []
    for item in value:
        out.append(capo_managedblockchain.types.network_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkSummaryList:
    import capo_managedblockchain.types.network_summary

    out: NetworkSummaryList = []
    for item in data:
        out.append(capo_managedblockchain.types.network_summary.deserialize_json(item))
    return out
