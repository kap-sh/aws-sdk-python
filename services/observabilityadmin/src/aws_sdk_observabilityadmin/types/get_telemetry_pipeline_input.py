"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetTelemetryPipelineInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_identifier


class GetTelemetryPipelineInput(TypedDict):
    pipeline_identifier: "aws_sdk_observabilityadmin.types.telemetry_pipeline_identifier.TelemetryPipelineIdentifier"
    """<p>The identifier (name or ARN) of the telemetry pipeline to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTelemetryPipelineInput) -> dict:
    out: dict = {}
    out["PipelineIdentifier"] = value["pipeline_identifier"]
    return out


def deserialize_json(data: dict) -> GetTelemetryPipelineInput:
    out: GetTelemetryPipelineInput = {}  # type: ignore[typeddict-item]
    if "PipelineIdentifier" in data:
        out["pipeline_identifier"] = data["PipelineIdentifier"]
    else:
        raise DeserializationError(
            "GetTelemetryPipelineInput.pipeline_identifier required"
        )
    return out
