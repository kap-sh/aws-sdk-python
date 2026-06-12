"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateBandwidthRateLimitScheduleInput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals
    import aws_sdk_storage_gateway.types.gateway_arn


class UpdateBandwidthRateLimitScheduleInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    bandwidth_rate_limit_intervals: "aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals.BandwidthRateLimitIntervals"
    """<p> An array containing bandwidth rate limit schedule intervals for a gateway. When no bandwidth rate limit intervals have been scheduled, the array is empty. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBandwidthRateLimitScheduleInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    import aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals

    out["BandwidthRateLimitIntervals"] = (
        aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals.serialize_aws_json_1_1(
            value["bandwidth_rate_limit_intervals"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBandwidthRateLimitScheduleInput:
    out: UpdateBandwidthRateLimitScheduleInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError(
            "UpdateBandwidthRateLimitScheduleInput.gateway_arn required"
        )
    if "BandwidthRateLimitIntervals" in data:
        import aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals

        out["bandwidth_rate_limit_intervals"] = (
            aws_sdk_storage_gateway.types.bandwidth_rate_limit_intervals.deserialize_aws_json_1_1(
                data["BandwidthRateLimitIntervals"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateBandwidthRateLimitScheduleInput.bandwidth_rate_limit_intervals required"
        )
    return out
