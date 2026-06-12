"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PredictiveConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.bandwidth_allocation


class PredictiveConfig(TypedDict):
    bandwidth_allocation: (
        "aws_sdk_connectcampaignsv2.types.bandwidth_allocation.BandwidthAllocation"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PredictiveConfig) -> dict:
    out: dict = {}
    out["bandwidthAllocation"] = value["bandwidth_allocation"]
    return out


def deserialize_json(data: dict) -> PredictiveConfig:
    out: PredictiveConfig = {}  # type: ignore[typeddict-item]
    if "bandwidthAllocation" in data:
        out["bandwidth_allocation"] = data["bandwidthAllocation"]
    else:
        raise DeserializationError("PredictiveConfig.bandwidth_allocation required")
    return out
