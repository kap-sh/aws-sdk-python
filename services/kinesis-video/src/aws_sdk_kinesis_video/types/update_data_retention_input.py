"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#UpdateDataRetentionInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_video.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_video.types.data_retention_change_in_hours
    import aws_sdk_kinesis_video.types.resource_arn
    import aws_sdk_kinesis_video.types.stream_name
    import aws_sdk_kinesis_video.types.update_data_retention_operation
    import aws_sdk_kinesis_video.types.version


class UpdateDataRetentionInput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream whose retention period you want to change.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream whose retention period you want to change.</p>"""
    current_version: "aws_sdk_kinesis_video.types.version.Version"
    """<p>The version of the stream whose retention period you want to change. To get the version, call either the <code>DescribeStream</code> or the <code>ListStreams</code> API.</p>"""
    operation: "aws_sdk_kinesis_video.types.update_data_retention_operation.UpdateDataRetentionOperation"
    """<p>Indicates whether you want to increase or decrease the retention period.</p>"""
    data_retention_change_in_hours: "aws_sdk_kinesis_video.types.data_retention_change_in_hours.DataRetentionChangeInHours"
    """<p>The number of hours to adjust the current retention by. The value you specify is added to or subtracted from the current value, depending on the <code>operation</code>.</p> <p>The minimum value for data retention is 0 and the maximum value is 87600 (ten years).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataRetentionInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    out["CurrentVersion"] = value["current_version"]
    import aws_sdk_kinesis_video.types.update_data_retention_operation

    out["Operation"] = (
        aws_sdk_kinesis_video.types.update_data_retention_operation.serialize_json(
            value["operation"]
        )
    )
    out["DataRetentionChangeInHours"] = value["data_retention_change_in_hours"]
    return out


def deserialize_json(data: dict) -> UpdateDataRetentionInput:
    out: UpdateDataRetentionInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "CurrentVersion" in data:
        out["current_version"] = data["CurrentVersion"]
    else:
        raise DeserializationError("UpdateDataRetentionInput.current_version required")
    if "Operation" in data:
        import aws_sdk_kinesis_video.types.update_data_retention_operation

        out["operation"] = (
            aws_sdk_kinesis_video.types.update_data_retention_operation.deserialize_json(
                data["Operation"]
            )
        )
    else:
        raise DeserializationError("UpdateDataRetentionInput.operation required")
    if "DataRetentionChangeInHours" in data:
        out["data_retention_change_in_hours"] = data["DataRetentionChangeInHours"]
    else:
        raise DeserializationError(
            "UpdateDataRetentionInput.data_retention_change_in_hours required"
        )
    return out
