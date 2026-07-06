"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.tag_map_output
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_name
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_status
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_status_reason


class TelemetryPipeline(TypedDict, closed=True):
    created_time_stamp: NotRequired["int"]
    """<p>The timestamp when the telemetry pipeline was created.</p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p>The timestamp when the telemetry pipeline was last updated.</p>"""
    arn: NotRequired["aws_sdk_observabilityadmin.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the telemetry pipeline.</p>"""
    name: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_pipeline_name.TelemetryPipelineName"
    ]
    """<p>The name of the telemetry pipeline.</p>"""
    configuration: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.TelemetryPipelineConfiguration"
    ]
    """<p>The configuration that defines how the telemetry pipeline processes data.</p>"""
    status: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_pipeline_status.TelemetryPipelineStatus"
    ]
    """<p>The current status of the telemetry pipeline.</p>"""
    status_reason: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_pipeline_status_reason.TelemetryPipelineStatusReason"
    ]
    """<p>Additional information about the pipeline status, including reasons for failure states.</p>"""
    tags: NotRequired["aws_sdk_observabilityadmin.types.tag_map_output.TagMapOutput"]
    """<p>The key-value pairs associated with the telemetry pipeline resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipeline) -> dict:
    out: dict = {}
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "configuration" in value:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

        out["Configuration"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "status" in value:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_status

        out["Status"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_status.serialize_json(
                value["status"]
            )
        )
    if "status_reason" in value:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_status_reason

        out["StatusReason"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_status_reason.serialize_json(
                value["status_reason"]
            )
        )
    if "tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_output

        out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_output.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> TelemetryPipeline:
    out: TelemetryPipeline = {}  # type: ignore[typeddict-item]
    if "CreatedTimeStamp" in data:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    if "LastUpdateTimeStamp" in data:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Configuration" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration

        out["configuration"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_configuration.deserialize_json(
                data["Configuration"]
            )
        )
    if "Status" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_status

        out["status"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_status.deserialize_json(
                data["Status"]
            )
        )
    if "StatusReason" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_status_reason

        out["status_reason"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_output

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_output.deserialize_json(
            data["Tags"]
        )
    return out
