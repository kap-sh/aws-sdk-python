"""Generated from Smithy shape ``com.amazonaws.sesv2#PutDedicatedIpWarmupAttributesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_sesv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.ip
    import aws_sdk_sesv2.types.percentage100_wrapper


class PutDedicatedIpWarmupAttributesRequest(TypedDict, closed=True):
    ip: "aws_sdk_sesv2.types.ip.Ip"
    """<p>The dedicated IP address that you want to update the warm-up attributes for.</p>"""
    warmup_percentage: "aws_sdk_sesv2.types.percentage100_wrapper.Percentage100Wrapper"
    """<p>The warm-up percentage that you want to associate with the dedicated IP address.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutDedicatedIpWarmupAttributesRequest) -> dict:
    out: dict = {}
    out["WarmupPercentage"] = value["warmup_percentage"]
    return out


def deserialize_json(data: dict) -> PutDedicatedIpWarmupAttributesRequest:
    out: PutDedicatedIpWarmupAttributesRequest = {}  # type: ignore[typeddict-item]
    if "WarmupPercentage" in data:
        out["warmup_percentage"] = data["WarmupPercentage"]
    else:
        raise DeserializationError(
            "PutDedicatedIpWarmupAttributesRequest.warmup_percentage required"
        )
    return out
