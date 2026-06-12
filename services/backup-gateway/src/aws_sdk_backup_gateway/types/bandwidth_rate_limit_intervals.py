"""Generated from Smithy shape ``com.amazonaws.backupgateway#BandwidthRateLimitIntervals``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_backup_gateway.types.bandwidth_rate_limit_interval

BandwidthRateLimitIntervals: TypeAlias = list[
    "aws_sdk_backup_gateway.types.bandwidth_rate_limit_interval.BandwidthRateLimitInterval"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BandwidthRateLimitIntervals) -> list:
    import aws_sdk_backup_gateway.types.bandwidth_rate_limit_interval

    out: list = []
    for item in value:
        out.append(
            aws_sdk_backup_gateway.types.bandwidth_rate_limit_interval.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> BandwidthRateLimitIntervals:
    import aws_sdk_backup_gateway.types.bandwidth_rate_limit_interval

    out: BandwidthRateLimitIntervals = []
    for item in data:
        out.append(
            aws_sdk_backup_gateway.types.bandwidth_rate_limit_interval.deserialize_aws_json_1_0(
                item
            )
        )
    return out
