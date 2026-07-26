"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeBandwidthRateLimitOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.bandwidth_download_rate_limit
    import capo_storage_gateway.types.bandwidth_upload_rate_limit
    import capo_storage_gateway.types.gateway_arn


class DescribeBandwidthRateLimitOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    average_upload_rate_limit_in_bits_per_sec: NotRequired[
        "capo_storage_gateway.types.bandwidth_upload_rate_limit.BandwidthUploadRateLimit"
    ]
    """<p>The average upload bandwidth rate limit in bits per second. This field does not appear in the response if the upload rate limit is not set.</p>"""
    average_download_rate_limit_in_bits_per_sec: NotRequired[
        "capo_storage_gateway.types.bandwidth_download_rate_limit.BandwidthDownloadRateLimit"
    ]
    """<p>The average download bandwidth rate limit in bits per second. This field does not appear in the response if the download rate limit is not set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeBandwidthRateLimitOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
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


def deserialize_aws_json_1_1(data: dict) -> DescribeBandwidthRateLimitOutput:
    out: DescribeBandwidthRateLimitOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "AverageUploadRateLimitInBitsPerSec" in data:
        out["average_upload_rate_limit_in_bits_per_sec"] = data[
            "AverageUploadRateLimitInBitsPerSec"
        ]
    if "AverageDownloadRateLimitInBitsPerSec" in data:
        out["average_download_rate_limit_in_bits_per_sec"] = data[
            "AverageDownloadRateLimitInBitsPerSec"
        ]
    return out
