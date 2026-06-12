"""Generated from Smithy shape ``com.amazonaws.oam#ResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_oam.errors import DeserializationError

ResourceType: TypeAlias = Literal[
    "AWS::CloudWatch::Metric",
    "AWS::Logs::LogGroup",
    "AWS::XRay::Trace",
    "AWS::ApplicationInsights::Application",
    "AWS::InternetMonitor::Monitor",
    "AWS::ApplicationSignals::Service",
    "AWS::ApplicationSignals::ServiceLevelObjective",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS::CloudWatch::Metric",
        "AWS::Logs::LogGroup",
        "AWS::XRay::Trace",
        "AWS::ApplicationInsights::Application",
        "AWS::InternetMonitor::Monitor",
        "AWS::ApplicationSignals::Service",
        "AWS::ApplicationSignals::ServiceLevelObjective",
    )
)


def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceType value: {data!r}")
    return cast(ResourceType, data)
