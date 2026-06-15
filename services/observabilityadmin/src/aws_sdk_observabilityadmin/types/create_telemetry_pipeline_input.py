"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateTelemetryPipelineInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.tag_map_input
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_name


class CreateTelemetryPipelineInput(TypedDict):
    name: (
        "aws_sdk_observabilityadmin.types.telemetry_pipeline_name.TelemetryPipelineName"
    )
    """<p>The name of the telemetry pipeline to create. The name must be unique within your account.</p>"""
    configuration: "aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration"
    r"""<p>The configuration that defines how the telemetry pipeline processes data, including sources, processors, and destinations. For more information about pipeline components, see the <a href=\"https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/pipeline-components-reference.html\">Amazon CloudWatch User Guide</a> </p>"""
    tags: NotRequired["aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p>The key-value pairs to associate with the telemetry pipeline resource for categorization and management purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTelemetryPipelineInput) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

    out["Configuration"] = (
        aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateTelemetryPipelineInput:
    out: CreateTelemetryPipelineInput = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateTelemetryPipelineInput.name required")
    if "Configuration" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

        out["configuration"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateTelemetryPipelineInput.configuration required"
        )
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    return out
