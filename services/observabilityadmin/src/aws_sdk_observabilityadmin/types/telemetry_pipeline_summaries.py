"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipelineSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_summary

TelemetryPipelineSummaries: TypeAlias = list[
    "aws_sdk_observabilityadmin.types.telemetry_pipeline_summary.TelemetryPipelineSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipelineSummaries) -> list:
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_pipeline_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TelemetryPipelineSummaries:
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_summary

    out: TelemetryPipelineSummaries = []
    for item in data:
        out.append(
            aws_sdk_observabilityadmin.types.telemetry_pipeline_summary.deserialize_json(
                item
            )
        )
    return out
