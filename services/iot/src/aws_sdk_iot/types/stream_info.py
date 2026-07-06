"""Generated from Smithy shape ``com.amazonaws.iot#StreamInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.stream_arn
    import aws_sdk_iot.types.stream_description
    import aws_sdk_iot.types.stream_files
    import aws_sdk_iot.types.stream_id
    import aws_sdk_iot.types.stream_version


class StreamInfo(TypedDict, closed=True):
    stream_id: NotRequired["aws_sdk_iot.types.stream_id.StreamId"]
    """<p>The stream ID.</p>"""
    stream_arn: NotRequired["aws_sdk_iot.types.stream_arn.StreamArn"]
    """<p>The stream ARN.</p>"""
    stream_version: NotRequired["aws_sdk_iot.types.stream_version.StreamVersion"]
    """<p>The stream version.</p>"""
    description: NotRequired["aws_sdk_iot.types.stream_description.StreamDescription"]
    """<p>The description of the stream.</p>"""
    files: NotRequired["aws_sdk_iot.types.stream_files.StreamFiles"]
    """<p>The files to stream.</p>"""
    created_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the stream was created.</p>"""
    last_updated_at: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The date when the stream was last updated.</p>"""
    role_arn: NotRequired["aws_sdk_iot.types.role_arn.RoleArn"]
    """<p>An IAM role IoT assumes to access your S3 files.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StreamInfo) -> dict:
    out: dict = {}
    if "stream_id" in value:
        out["streamId"] = value["stream_id"]
    if "stream_arn" in value:
        out["streamArn"] = value["stream_arn"]
    if "stream_version" in value:
        out["streamVersion"] = value["stream_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "files" in value:
        import aws_sdk_iot.types.stream_files

        out["files"] = aws_sdk_iot.types.stream_files.serialize_json(value["files"])
    if "created_at" in value:
        import aws_sdk_iot.types.date_type

        out["createdAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_iot.types.date_type

        out["lastUpdatedAt"] = aws_sdk_iot.types.date_type.serialize_json(
            value["last_updated_at"]
        )
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> StreamInfo:
    out: StreamInfo = {}  # type: ignore[typeddict-item]
    if "streamId" in data:
        out["stream_id"] = data["streamId"]
    if "streamArn" in data:
        out["stream_arn"] = data["streamArn"]
    if "streamVersion" in data:
        out["stream_version"] = data["streamVersion"]
    if "description" in data:
        out["description"] = data["description"]
    if "files" in data:
        import aws_sdk_iot.types.stream_files

        out["files"] = aws_sdk_iot.types.stream_files.deserialize_json(data["files"])
    if "createdAt" in data:
        import aws_sdk_iot.types.date_type

        out["created_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["createdAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_iot.types.date_type

        out["last_updated_at"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
