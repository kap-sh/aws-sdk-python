"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeBandwidthRateLimitScheduleOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals
    import aws_sdk_storage_gateway.types.gateway_arn


class DescribeBandwidthRateLimitScheduleOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]
    bandwidth_rate_limit_intervals: NotRequired[
        "aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals.BandwidthRateLimitIntervals"
    ]
    """<p> An array that contains the bandwidth rate limit intervals for a tape or volume gateway. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBandwidthRateLimitScheduleOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "bandwidth_rate_limit_intervals" in value:
        import aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals

        out["BandwidthRateLimitIntervals"] = (
            aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals.serialize_aws_json_1_1(
                value["bandwidth_rate_limit_intervals"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeBandwidthRateLimitScheduleOutput:
    out: DescribeBandwidthRateLimitScheduleOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "BandwidthRateLimitIntervals" in data:
        import aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals

        out["bandwidth_rate_limit_intervals"] = (
            aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals.deserialize_aws_json_1_1(
                data["BandwidthRateLimitIntervals"]
            )
        )
    return out
