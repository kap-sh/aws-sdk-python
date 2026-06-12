"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryRuleSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_rule_summary

TelemetryRuleSummaries: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.telemetry_rule_summary.TelemetryRuleSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryRuleSummaries) -> list:
    import aws_sdk_observabilityadmin.types.telemetry_rule_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_rule_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TelemetryRuleSummaries:
    import aws_sdk_observabilityadmin.types.telemetry_rule_summary

    out: TelemetryRuleSummaries = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_rule_summary.deserialize_json(
                item
            )
        )
    return out
