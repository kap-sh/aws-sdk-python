"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryPipelineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.configuration_summary
    import aws_sdk_observabilityadmin.types.resource_arn
    import aws_sdk_observabilityadmin.types.tag_map_output
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_name
    import aws_sdk_observabilityadmin.types.telemetry_pipeline_status


class TelemetryPipelineSummary(TypedDict, closed=True):
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
    status: NotRequired[
        "aws_sdk_observabilityadmin.types.telemetry_pipeline_status.TelemetryPipelineStatus"
    ]
    """<p>The current status of the telemetry pipeline.</p>"""
    tags: NotRequired["aws_sdk_observabilityadmin.types.tag_map_output.TagMapOutput"]
    """<p>The key-value pairs associated with the telemetry pipeline resource.</p>"""
    configuration_summary: NotRequired[
        "aws_sdk_observabilityadmin.types.configuration_summary.ConfigurationSummary"
    ]
    """<p>A summary of the pipeline configuration components.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryPipelineSummary) -> dict:
    out: dict = {}
    if "created_time_stamp" in value:
        out["CreatedTimeStamp"] = value["created_time_stamp"]
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_status

        out["Status"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_status.serialize_json(
                value["status"]
            )
        )
    if "tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_output

        out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_output.serialize_json(
            value["tags"]
        )
    if "configuration_summary" in value:
        import aws_sdk_observabilityadmin.types.configuration_summary

        out["ConfigurationSummary"] = (
            aws_sdk_observabilityadmin.types.configuration_summary.serialize_json(
                value["configuration_summary"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryPipelineSummary:
    out: TelemetryPipelineSummary = {}  # type: ignore[typeddict-item]
    if "CreatedTimeStamp" in data:
        out["created_time_stamp"] = data["CreatedTimeStamp"]
    if "LastUpdateTimeStamp" in data:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_observabilityadmin.types.telemetry_pipeline_status

        out["status"] = (
            aws_sdk_observabilityadmin.types.telemetry_pipeline_status.deserialize_json(
                data["Status"]
            )
        )
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_output

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_output.deserialize_json(
            data["Tags"]
        )
    if "ConfigurationSummary" in data:
        import aws_sdk_observabilityadmin.types.configuration_summary

        out["configuration_summary"] = (
            aws_sdk_observabilityadmin.types.configuration_summary.deserialize_json(
                data["ConfigurationSummary"]
            )
        )
    return out
