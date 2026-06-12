"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConnectPeerSummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.connect_peer_summary

ConnectPeerSummaryList: TypeAlias = list[
    "aws_sdk_networkmanager.types.connect_peer_summary.ConnectPeerSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConnectPeerSummaryList) -> list:
    import aws_sdk_networkmanager.types.connect_peer_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.connect_peer_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ConnectPeerSummaryList:
    import aws_sdk_networkmanager.types.connect_peer_summary

    out: ConnectPeerSummaryList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.connect_peer_summary.deserialize_json(item)
        )
    return out
