"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ValidateTelemetryPipelineConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration


class ValidateTelemetryPipelineConfigurationInput(TypedDict, closed=True):
    configuration: "aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration"
    """<p>The pipeline configuration to validate for syntax and compatibility.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateTelemetryPipelineConfigurationInput) -> dict:
    out: dict = {}
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

    out["Configuration"] = (
        aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ValidateTelemetryPipelineConfigurationInput:
    out: ValidateTelemetryPipelineConfigurationInput = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

        out["configuration"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "ValidateTelemetryPipelineConfigurationInput.configuration required"
        )
    return out
