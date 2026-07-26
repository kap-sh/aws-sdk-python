"""Generated from Smithy shape ``com.amazonaws.groundstation#ConfigCapabilityType``."""

from typing import Literal, TypeAlias, cast

ConfigCapabilityType: TypeAlias = Literal[
    "antenna-downlink",
    "antenna-downlink-demod-decode",
    "tracking",
    "dataflow-endpoint",
    "antenna-uplink",
    "uplink-echo",
    "s3-recording",
    "telemetry-sink",
]


# --- restJson1 ser/de ---
def serialize_json(value: ConfigCapabilityType) -> str:
    return value


def deserialize_json(data: str) -> ConfigCapabilityType:
    return cast(ConfigCapabilityType, data)
