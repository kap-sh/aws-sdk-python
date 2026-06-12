"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateTelemetryPipelineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn


class CreateTelemetryPipelineOutput(TypedDict):
    arn: NotRequired["aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the created telemetry pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTelemetryPipelineOutput) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_json(data: dict) -> CreateTelemetryPipelineOutput:
    out: CreateTelemetryPipelineOutput = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
