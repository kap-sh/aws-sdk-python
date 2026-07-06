"""Generated from Smithy shape ``com.amazonaws.appmesh#FileAccessLog``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.file_path
    import aws_sdk_app_mesh.types.logging_format


class FileAccessLog(TypedDict, closed=True):
    path: "aws_sdk_app_mesh.types.file_path.FilePath"
    """<p>The file path to write access logs to. You can use <code>/dev/stdout</code> to send access logs to standard out and configure your Envoy container to use a log driver, such as <code>awslogs</code>, to export the access logs to a log storage service such as Amazon CloudWatch Logs. You can also specify a path in the Envoy container's file system to write the files to disk.</p> <note> <p>The Envoy process must have write permissions to the path that you specify here. Otherwise, Envoy fails to bootstrap properly.</p> </note>"""
    format: NotRequired["aws_sdk_app_mesh.types.logging_format.LoggingFormat"]
    """<p>The specified format for the logs. The format is either <code>json_format</code> or <code>text_format</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileAccessLog) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    if "format" in value:
        import aws_sdk_app_mesh.types.logging_format

        out["format"] = aws_sdk_app_mesh.types.logging_format.serialize_json(
            value["format"]
        )
    return out


def deserialize_json(data: dict) -> FileAccessLog:
    out: FileAccessLog = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("FileAccessLog.path required")
    if "format" in data:
        import aws_sdk_app_mesh.types.logging_format

        out["format"] = aws_sdk_app_mesh.types.logging_format.deserialize_json(
            data["format"]
        )
    return out
