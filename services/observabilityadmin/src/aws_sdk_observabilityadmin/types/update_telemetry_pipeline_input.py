"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#UpdateTelemetryPipelineInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_identifier


class UpdateTelemetryPipelineInput(TypedDict):
    pipeline_identifier: "aws_sdk_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier"
    """<p>The ARN of the telemetry pipeline to update.</p>"""
    configuration: "aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration"
    """<p>The new configuration for the telemetry pipeline, including updated sources, processors, and destinations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTelemetryPipelineInput) -> dict:
    out: dict = {}
    out["PipelineIdentifier"] = value["pipeline_identifier"]
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

    out["Configuration"] = (
        aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateTelemetryPipelineInput:
    out: UpdateTelemetryPipelineInput = {}  # type: ignore[typeddict-item]
    if "PipelineIdentifier" in data:
        out["pipeline_identifier"] = data["PipelineIdentifier"]
    else:
        raise DeserializationError(
            "UpdateTelemetryPipelineInput.pipeline_identifier required"
        )
    if "Configuration" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

        out["configuration"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateTelemetryPipelineInput.configuration required"
        )
    return out
