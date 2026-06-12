"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesNumberField``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "FindingsSummary.TotalFindings",
        "FindingsSummary.Severities.Other",
        "FindingsSummary.Severities.Fatal",
        "FindingsSummary.Severities.Critical",
        "FindingsSummary.Severities.High",
        "FindingsSummary.Severities.Medium",
        "FindingsSummary.Severities.Low",
        "FindingsSummary.Severities.Informational",
        "FindingsSummary.Severities.Unknown",
    )
)


def serialize_json(value: ResourcesNumberField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesNumberField:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourcesNumberField value: {data!r}")
    return cast(ResourcesNumberField, data)
