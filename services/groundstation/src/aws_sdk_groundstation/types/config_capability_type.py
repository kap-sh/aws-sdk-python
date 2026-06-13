"""Generated from Smithy shape ``com.amazonaws.groundstation#ConfigCapabilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_groundstation.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "antenna-downlink",
        "antenna-downlink-demod-decode",
        "tracking",
        "dataflow-endpoint",
        "antenna-uplink",
        "uplink-echo",
        "s3-recording",
        "telemetry-sink",
    )
)


def serialize_json(value: ConfigCapabilityType) -> str:
    return value


def deserialize_json(data: str) -> ConfigCapabilityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigCapabilityType value: {data!r}")
    return cast(ConfigCapabilityType, data)
