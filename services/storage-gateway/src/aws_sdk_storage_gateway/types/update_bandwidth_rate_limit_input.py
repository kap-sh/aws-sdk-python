"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateBandwidthRateLimitInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.bandwidth_download_rate_limit
    import aws_sdk_storage_gateway.types.bandwidth_upload_rate_limit
    import aws_sdk_storage_gateway.types.gateway_arn


class UpdateBandwidthRateLimitInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"
    average_upload_rate_limit_in_bits_per_sec: NotRequired[
        "aws_sdk_storage_gateway.types.bandwidth_upload_rate_limit.BandwidthUploadRateLimit"
    ]
    """<p>The average upload bandwidth rate limit in bits per second.</p>"""
    average_download_rate_limit_in_bits_per_sec: NotRequired[
        "aws_sdk_storage_gateway.types.bandwidth_download_rate_limit.BandwidthDownloadRateLimit"
    ]
    """<p>The average download bandwidth rate limit in bits per second.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBandwidthRateLimitInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    if "average_upload_rate_limit_in_bits_per_sec" in value:
        out["AverageUploadRateLimitInBitsPerSec"] = value[
            "average_upload_rate_limit_in_bits_per_sec"
        ]
    if "average_download_rate_limit_in_bits_per_sec" in value:
        out["AverageDownloadRateLimitInBitsPerSec"] = value[
            "average_download_rate_limit_in_bits_per_sec"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateBandwidthRateLimitInput:
    out: UpdateBandwidthRateLimitInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("UpdateBandwidthRateLimitInput.gateway_arn required")
    if "AverageUploadRateLimitInBitsPerSec" in data:
        out["average_upload_rate_limit_in_bits_per_sec"] = data[
            "AverageUploadRateLimitInBitsPerSec"
        ]
    if "AverageDownloadRateLimitInBitsPerSec" in data:
        out["average_download_rate_limit_in_bits_per_sec"] = data[
            "AverageDownloadRateLimitInBitsPerSec"
        ]
    return out
