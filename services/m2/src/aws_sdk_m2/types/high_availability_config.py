"""Generated from Smithy shape ``com.amazonaws.m2#HighAvailabilityConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_m2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_m2.types.capacity_value


class HighAvailabilityConfig(TypedDict):
    desired_capacity: "aws_sdk_m2.types.capacity_value.CapacityValue"
    """<p>The number of instances in a high availability configuration. The minimum possible value is 1 and the maximum is 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HighAvailabilityConfig) -> dict:
    out: dict = {}
    out["desiredCapacity"] = value["desired_capacity"]
    return out


def deserialize_json(data: dict) -> HighAvailabilityConfig:
    out: HighAvailabilityConfig = {}  # type: ignore[typeddict-item]
    if "desiredCapacity" in data:
        out["desired_capacity"] = data["desiredCapacity"]
    else:
        raise DeserializationError("HighAvailabilityConfig.desired_capacity required")
    return out
