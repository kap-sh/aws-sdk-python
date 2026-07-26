"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesNumberField``."""

from typing import Literal, TypeAlias, cast

ResourcesNumberField: TypeAlias = Literal[
    "FindingsSummary.TotalFindings",
    "FindingsSummary.Severities.Other",
    "FindingsSummary.Severities.Fatal",
    "FindingsSummary.Severities.Critical",
    "FindingsSummary.Severities.High",
    "FindingsSummary.Severities.Medium",
    "FindingsSummary.Severities.Low",
    "FindingsSummary.Severities.Informational",
    "FindingsSummary.Severities.Unknown",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesNumberField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesNumberField:
    return cast(ResourcesNumberField, data)
