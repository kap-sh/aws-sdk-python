"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_summary

CoreNetworkSummaryList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_summary.CoreNetworkSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkSummaryList) -> list:
    import aws_sdk_networkmanager.types.core_network_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoreNetworkSummaryList:
    import aws_sdk_networkmanager.types.core_network_summary

    out: CoreNetworkSummaryList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_summary.deserialize_json(item)
        )
    return out
