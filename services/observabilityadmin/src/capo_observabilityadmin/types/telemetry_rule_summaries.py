"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryRuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_rule_summary

TelemetryRuleSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.telemetry_rule_summary.TelemetryRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRuleSummaries) -> list:
    import capo_observabilityadmin.types.telemetry_rule_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.telemetry_rule_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TelemetryRuleSummaries:
    import capo_observabilityadmin.types.telemetry_rule_summary

    out: TelemetryRuleSummaries = []
    for item in data:
        out.append(
            capo_observabilityadmin.types.telemetry_rule_summary.deserialize_json(item)
        )
    return out
