"""Generated from Smithy shape ``com.amazonaws.interconnect#BandwidthList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_interconnect.types.connection_bandwidth

BandwidthList: TypeAlias = list[
    "aws_sdk_interconnect.types.connection_bandwidth.ConnectionBandwidth"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BandwidthList) -> list:
    return list(value)


def deserialize_aws_json_1_0(data: list) -> BandwidthList:
    return list(data)
