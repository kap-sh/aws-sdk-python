"""Generated from Smithy shape ``com.amazonaws.managedblockchain#NetworkSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.network_summary

NetworkSummaryList: TypeAlias = list[
    "aws_sdk_managedblockchain.types.network_summary.NetworkSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: NetworkSummaryList) -> list:
    import aws_sdk_managedblockchain.types.network_summary

    out: list = []
    for item in value:
        out.append(aws_sdk_managedblockchain.types.network_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> NetworkSummaryList:
    import aws_sdk_managedblockchain.types.network_summary

    out: NetworkSummaryList = []
    for item in data:
        out.append(
            aws_sdk_managedblockchain.types.network_summary.deserialize_json(item)
        )
    return out
