"""Generated from Smithy shape ``com.amazonaws.osis#PipelineSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.pipeline_arn
    import aws_sdk_osis.types.pipeline_destination_list
    import aws_sdk_osis.types.pipeline_name
    import aws_sdk_osis.types.pipeline_status
    import aws_sdk_osis.types.pipeline_status_reason
    import aws_sdk_osis.types.pipeline_units
    import aws_sdk_osis.types.tag_list
    import aws_sdk_osis.types.timestamp


class PipelineSummary(TypedDict, closed=True):
    status: NotRequired["aws_sdk_osis.types.pipeline_status.PipelineStatus"]
    """<p>The current status of the pipeline.</p>"""
    status_reason: NotRequired[
        "aws_sdk_osis.types.pipeline_status_reason.PipelineStatusReason"
    ]
    pipeline_name: NotRequired["aws_sdk_osis.types.pipeline_name.PipelineName"]
    """<p>The name of the pipeline.</p>"""
    pipeline_arn: NotRequired["aws_sdk_osis.types.pipeline_arn.PipelineArn"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    min_units: NotRequired["aws_sdk_osis.types.pipeline_units.PipelineUnits"]
    """<p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    max_units: NotRequired["aws_sdk_osis.types.pipeline_units.PipelineUnits"]
    """<p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    created_at: NotRequired["aws_sdk_osis.types.timestamp.Timestamp"]
    """<p>The date and time when the pipeline was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_osis.types.timestamp.Timestamp"]
    """<p>The date and time when the pipeline was last updated.</p>"""
    destinations: NotRequired[
        "aws_sdk_osis.types.pipeline_destination_list.PipelineDestinationList"
    ]
    """<p>A list of destinations to which the pipeline writes data.</p>"""
    tags: NotRequired["aws_sdk_osis.types.tag_list.TagList"]
    """<p>A list of tags associated with the given pipeline.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineSummary) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_osis.types.pipeline_status

        out["Status"] = aws_sdk_osis.types.pipeline_status.serialize_json(
            value["status"]
        )
    if "status_reason" in value:
        import aws_sdk_osis.types.pipeline_status_reason

        out["StatusReason"] = aws_sdk_osis.types.pipeline_status_reason.serialize_json(
            value["status_reason"]
        )
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    if "min_units" in value:
        out["MinUnits"] = value["min_units"]
    if "max_units" in value:
        out["MaxUnits"] = value["max_units"]
    if "created_at" in value:
        import aws_sdk_osis.types.timestamp

        out["CreatedAt"] = aws_sdk_osis.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_osis.types.timestamp

        out["LastUpdatedAt"] = aws_sdk_osis.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "destinations" in value:
        import aws_sdk_osis.types.pipeline_destination_list

        out["Destinations"] = (
            aws_sdk_osis.types.pipeline_destination_list.serialize_json(
                value["destinations"]
            )
        )
    if "tags" in value:
        import aws_sdk_osis.types.tag_list

        out["Tags"] = aws_sdk_osis.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> PipelineSummary:
    out: PipelineSummary = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import aws_sdk_osis.types.pipeline_status

        out["status"] = aws_sdk_osis.types.pipeline_status.deserialize_json(
            data["Status"]
        )
    if "StatusReason" in data:
        import aws_sdk_osis.types.pipeline_status_reason

        out["status_reason"] = (
            aws_sdk_osis.types.pipeline_status_reason.deserialize_json(
                data["StatusReason"]
            )
        )
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "MinUnits" in data:
        out["min_units"] = data["MinUnits"]
    if "MaxUnits" in data:
        out["max_units"] = data["MaxUnits"]
    if "CreatedAt" in data:
        import aws_sdk_osis.types.timestamp

        out["created_at"] = aws_sdk_osis.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_osis.types.timestamp

        out["last_updated_at"] = aws_sdk_osis.types.timestamp.deserialize_json(
            data["LastUpdatedAt"]
        )
    if "Destinations" in data:
        import aws_sdk_osis.types.pipeline_destination_list

        out["destinations"] = (
            aws_sdk_osis.types.pipeline_destination_list.deserialize_json(
                data["Destinations"]
            )
        )
    if "Tags" in data:
        import aws_sdk_osis.types.tag_list

        out["tags"] = aws_sdk_osis.types.tag_list.deserialize_json(data["Tags"])
    return out
