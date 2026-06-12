"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#ListEdgeAgentConfigurationsEdgeConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.edge_config
    import aws_sdk_kinesis_video.types.failed_status_details
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name
    import aws_sdk_kinesis_video.types.sync_status
    import aws_sdk_kinesis_video.types.timestamp


class ListEdgeAgentConfigurationsEdgeConfig(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""
    creation_time: NotRequired["aws_sdk_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp when the stream first created the edge config.</p>"""
    last_updated_time: NotRequired["aws_sdk_kinesis_video.types.timestamp.Timestamp"]
    """<p>The timestamp when the stream last updated the edge config.</p>"""
    sync_status: NotRequired["aws_sdk_kinesis_video.types.sync_status.SyncStatus"]
    """<p>The current sync status of the stream's edge configuration.</p>"""
    failed_status_details: NotRequired[
        "aws_sdk_kinesis_video.types.failed_status_details.FailedStatusDetails"
    ]
    """<p>A description of the generated failure status.</p>"""
    edge_config: NotRequired["aws_sdk_kinesis_video.types.edge_config.EdgeConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: ListEdgeAgentConfigurationsEdgeConfig) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "creation_time" in value:
        import aws_sdk_kinesis_video.types.timestamp

        out["CreationTime"] = aws_sdk_kinesis_video.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_kinesis_video.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_kinesis_video.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "sync_status" in value:
        import aws_sdk_kinesis_video.types.sync_status

        out["SyncStatus"] = aws_sdk_kinesis_video.types.sync_status.serialize_json(
            value["sync_status"]
        )
    if "failed_status_details" in value:
        out["FailedStatusDetails"] = value["failed_status_details"]
    if "edge_config" in value:
        import aws_sdk_kinesis_video.types.edge_config

        out["EdgeConfig"] = aws_sdk_kinesis_video.types.edge_config.serialize_json(
            value["edge_config"]
        )
    return out


def deserialize_json(data: dict) -> ListEdgeAgentConfigurationsEdgeConfig:
    out: ListEdgeAgentConfigurationsEdgeConfig = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "CreationTime" in data:
        import aws_sdk_kinesis_video.types.timestamp

        out["creation_time"] = aws_sdk_kinesis_video.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_kinesis_video.types.timestamp

        out["last_updated_time"] = (
            aws_sdk_kinesis_video.types.timestamp.deserialize_json(
                data["LastUpdatedTime"]
            )
        )
    if "SyncStatus" in data:
        import aws_sdk_kinesis_video.types.sync_status

        out["sync_status"] = aws_sdk_kinesis_video.types.sync_status.deserialize_json(
            data["SyncStatus"]
        )
    if "FailedStatusDetails" in data:
        out["failed_status_details"] = data["FailedStatusDetails"]
    if "EdgeConfig" in data:
        import aws_sdk_kinesis_video.types.edge_config

        out["edge_config"] = aws_sdk_kinesis_video.types.edge_config.deserialize_json(
            data["EdgeConfig"]
        )
    return out
