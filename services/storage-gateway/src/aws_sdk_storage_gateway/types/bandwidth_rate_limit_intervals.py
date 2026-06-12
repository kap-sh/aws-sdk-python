"""Generated from Smithy shape ``com.amazonaws.storagegateway#BandwidthRateLimitIntervals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.bandwidth_rate_limit_interval

BandwidthRateLimitIntervals: TypeAlias = list[
    "aws_sdk_storage_gateway.types.bandwidth_rate_limit_interval.BandwidthRateLimitInterval"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BandwidthRateLimitIntervals) -> list:
    import aws_sdk_storage_gateway.types.bandwidth_rate_limit_interval

    out: list = []
    for item in value:
        out.append(
            aws_sdk_storage_gateway.types.bandwidth_rate_limit_interval.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BandwidthRateLimitIntervals:
    import aws_sdk_storage_gateway.types.bandwidth_rate_limit_interval

    out: BandwidthRateLimitIntervals = []
    for item in data:
        out.append(
            aws_sdk_storage_gateway.types.bandwidth_rate_limit_interval.deserialize_aws_json_1_1(
                item
            )
        )
    return out
