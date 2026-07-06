"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#PredictiveDialerConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connectcampaigns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaigns.types.bandwidth_allocation
    import aws_sdk_connectcampaigns.types.dialing_capacity


class PredictiveDialerConfig(TypedDict, closed=True):
    bandwidth_allocation: (
        "aws_sdk_connectcampaigns.types.bandwidth_allocation.BandwidthAllocation"
    )
    dialing_capacity: NotRequired[
        "aws_sdk_connectcampaigns.types.dialing_capacity.DialingCapacity"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: PredictiveDialerConfig) -> dict:
    out: dict = {}
    out["bandwidthAllocation"] = value["bandwidth_allocation"]
    if "dialing_capacity" in value:
        out["dialingCapacity"] = value["dialing_capacity"]
    return out


def deserialize_json(data: dict) -> PredictiveDialerConfig:
    out: PredictiveDialerConfig = {}  # type: ignore[typeddict-item]
    if "bandwidthAllocation" in data:
        out["bandwidth_allocation"] = data["bandwidthAllocation"]
    else:
        raise DeserializationError(
            "PredictiveDialerConfig.bandwidth_allocation required"
        )
    if "dialingCapacity" in data:
        out["dialing_capacity"] = data["dialingCapacity"]
    return out
