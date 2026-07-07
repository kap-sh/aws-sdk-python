"""Generated from Smithy shape ``com.amazonaws.iot#CreateStreamRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.role_arn
    import aws_sdk_iot.types.stream_description
    import aws_sdk_iot.types.stream_files
    import aws_sdk_iot.types.stream_id
    import aws_sdk_iot.types.tag_list


class CreateStreamRequest(TypedDict, closed=True):
    stream_id: "aws_sdk_iot.types.stream_id.StreamId"
    """<p>The stream ID.</p>"""
    description: NotRequired["aws_sdk_iot.types.stream_description.StreamDescription"]
    """<p>A description of the stream.</p>"""
    files: "aws_sdk_iot.types.stream_files.StreamFiles"
    """<p>The files to stream.</p>"""
    role_arn: "aws_sdk_iot.types.role_arn.RoleArn"
    """<p>An IAM role that allows the IoT service principal to access your S3 files.</p>"""
    tags: NotRequired["aws_sdk_iot.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage streams.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateStreamRequest) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_iot.types.stream_files

    out["files"] = aws_sdk_iot.types.stream_files.serialize_json(value["files"])
    out["roleArn"] = value["role_arn"]
    if "tags" in value:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateStreamRequest:
    out: CreateStreamRequest = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "files" in data:
        import aws_sdk_iot.types.stream_files

        out["files"] = aws_sdk_iot.types.stream_files.deserialize_json(data["files"])
    else:
        raise DeserializationError("CreateStreamRequest.files required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("CreateStreamRequest.role_arn required")
    if "tags" in data:
        import aws_sdk_iot.types.tag_list

        out["tags"] = aws_sdk_iot.types.tag_list.deserialize_json(data["tags"])
    return out
