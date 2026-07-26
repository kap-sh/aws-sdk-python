"""Generated from Smithy shape ``com.amazonaws.kinesisvideo#StreamInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_video.types.data_retention_in_hours
    import capo_kinesis_video.types.device_name
    import capo_kinesis_video.types.kms_key_id
    import capo_kinesis_video.types.media_type
    import capo_kinesis_video.types.resource_arn
    import capo_kinesis_video.types.status
    import capo_kinesis_video.types.stream_name
    import capo_kinesis_video.types.timestamp
    import capo_kinesis_video.types.version


class StreamInfo(TypedDict, closed=True):
    device_name: NotRequired["capo_kinesis_video.types.device_name.DeviceName"]
    """<p>The name of the device that is associated with the stream.</p>"""
    stream_name: NotRequired["capo_kinesis_video.types.stream_name.StreamName"]
    """<p>The name of the stream.</p>"""
    stream_arn: NotRequired["capo_kinesis_video.types.resource_arn.ResourceARN"]
    """<p>The Amazon Resource Name (ARN) of the stream.</p>"""
    media_type: NotRequired["capo_kinesis_video.types.media_type.MediaType"]
    """<p>The <code>MediaType</code> of the stream. </p>"""
    kms_key_id: NotRequired["capo_kinesis_video.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the Key Management Service (KMS) key that Kinesis Video Streams uses to encrypt data on the stream.</p>"""
    version: NotRequired["capo_kinesis_video.types.version.Version"]
    """<p>The version of the stream.</p>"""
    status: NotRequired["capo_kinesis_video.types.status.Status"]
    """<p>The status of the stream.</p>"""
    creation_time: NotRequired["capo_kinesis_video.types.timestamp.Timestamp"]
    """<p>A time stamp that indicates when the stream was created.</p>"""
    data_retention_in_hours: NotRequired[
        "capo_kinesis_video.types.data_retention_in_hours.DataRetentionInHours"
    ]
    """<p>How long the stream retains data, in hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamInfo) -> dict:
    out: dict = {}
    if "device_name" in value:
        out["DeviceName"] = value["device_name"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "media_type" in value:
        out["MediaType"] = value["media_type"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "version" in value:
        out["Version"] = value["version"]
    if "status" in value:
        import capo_kinesis_video.types.status

        out["Status"] = capo_kinesis_video.types.status.serialize_json(value["status"])
    if "creation_time" in value:
        import capo_kinesis_video.types.timestamp

        out["CreationTime"] = capo_kinesis_video.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "data_retention_in_hours" in value:
        out["DataRetentionInHours"] = value["data_retention_in_hours"]
    return out


def deserialize_json(data: dict) -> StreamInfo:
    out: StreamInfo = {}  # type: ignore[typeddict-item]
    if "DeviceName" in data:
        out["device_name"] = data["DeviceName"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "MediaType" in data:
        out["media_type"] = data["MediaType"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Status" in data:
        import capo_kinesis_video.types.status

        out["status"] = capo_kinesis_video.types.status.deserialize_json(data["Status"])
    if "CreationTime" in data:
        import capo_kinesis_video.types.timestamp

        out["creation_time"] = capo_kinesis_video.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    if "DataRetentionInHours" in data:
        out["data_retention_in_hours"] = data["DataRetentionInHours"]
    return out
