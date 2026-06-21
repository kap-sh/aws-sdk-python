"""Generated from Smithy shape ``com.amazonaws.iotwireless#SummaryMetricConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

SummaryMetricConfigurationStatus: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- restJson1 ser/de ---
def serialize_json(value: SummaryMetricConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> SummaryMetricConfigurationStatus:
    return cast(SummaryMetricConfigurationStatus, data)
