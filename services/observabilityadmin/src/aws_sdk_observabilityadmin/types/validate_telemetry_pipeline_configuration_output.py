"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ValidateTelemetryPipelineConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.validation_errors


class ValidateTelemetryPipelineConfigurationOutput(TypedDict, closed=True):
    errors: NotRequired[
        "aws_sdk_observabilityadmin.types.validation_errors.ValidationErrors"
    ]
    """<p>A list of validation errors found in the pipeline configuration, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidateTelemetryPipelineConfigurationOutput) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_observabilityadmin.types.validation_errors

        out["Errors"] = (
            aws_sdk_observabilityadmin.types.validation_errors.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValidateTelemetryPipelineConfigurationOutput:
    out: ValidateTelemetryPipelineConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "Errors" in data:
        import aws_sdk_observabilityadmin.types.validation_errors

        out["errors"] = (
            aws_sdk_observabilityadmin.types.validation_errors.deserialize_json(
                data["Errors"]
            )
        )
    return out
