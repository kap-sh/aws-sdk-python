"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipelineSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.telemetry_pipeline_summary

TelemetryPipelineSummaries: TypeAlias = list[
    "capo_observabilityadmin.types.telemetry_pipeline_summary.TelemetryPipelineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipelineSummaries) -> list:
    import capo_observabilityadmin.types.telemetry_pipeline_summary

    out: list = []
    for item in value:
        out.append(
            capo_observabilityadmin.types.telemetry_pipeline_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TelemetryPipelineSummaries:
    import capo_observabilityadmin.types.telemetry_pipeline_summary

    out: TelemetryPipelineSummaries = []
    for item in data:
        out.append(
            capo_observabilityadmin.types.telemetry_pipeline_summary.deserialize_json(
                item
            )
        )
    return out
