"""Generated from Smithy shape ``com.amazonaws.oam#ResourceType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
