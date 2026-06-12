"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#GetTelemetryPipelineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_pipeline


class GetTelemetryPipelineOutput(TypedDict):
    pipeline: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_pipeline.TelemetryPipeline"
    ]
    """<p>The complete telemetry pipeline resource information, including configuration, status, and metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTelemetryPipelineOutput) -> dict:
    out: dict = {}
    if "pipeline" in value:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline

        out["Pipeline"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline.serialize_json(
                value["pipeline"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTelemetryPipelineOutput:
    out: GetTelemetryPipelineOutput = {}  # type: ignore[typeddict-item]
    if "Pipeline" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline

        out["pipeline"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline.deserialize_json(
                data["Pipeline"]
            )
        )
    return out
