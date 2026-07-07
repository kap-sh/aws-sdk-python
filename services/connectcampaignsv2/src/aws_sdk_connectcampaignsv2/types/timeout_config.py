"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#TimeoutConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connectcampaignsv2.types.timeout_duration


class TimeoutConfig(TypedDict, closed=True):
    duration_in_seconds: (
        "aws_sdk_connectcampaignsv2.types.timeout_duration.TimeoutDuration"
    )


# --- restJson1 ser/de ---
def serialize_json(value: TimeoutConfig) -> dict:
    out: dict = {}
    out["durationInSeconds"] = value["duration_in_seconds"]
    return out


def deserialize_json(data: dict) -> TimeoutConfig:
    out: TimeoutConfig = {}  # type: ignore[typeddict-item]
    if "durationInSeconds" in data:
        out["duration_in_seconds"] = data["durationInSeconds"]
    else:
        raise DeserializationError("TimeoutConfig.duration_in_seconds required")
    return out
