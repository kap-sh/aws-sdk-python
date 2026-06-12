"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkSegmentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_segment

CoreNetworkSegmentList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_segment.CoreNetworkSegment"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkSegmentList) -> list:
    import aws_sdk_networkmanager.types.core_network_segment

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_segment.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoreNetworkSegmentList:
    import aws_sdk_networkmanager.types.core_network_segment

    out: CoreNetworkSegmentList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_segment.deserialize_json(item)
        )
    return out
