"""Generated from Smithy shape ``com.amazonaws.connect#ImportWorkspaceMediaRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.media_source
    import aws_sdk_connect.types.media_type
    import aws_sdk_connect.types.workspace_id


class ImportWorkspaceMediaRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Amazon Connect instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    workspace_id: "aws_sdk_connect.types.workspace_id.WorkspaceId"
    """<p>The identifier of the workspace.</p>"""
    media_type: "aws_sdk_connect.types.media_type.MediaType"
    """<p>The type of media. Valid values are: <code>IMAGE_LOGO_FAVICON</code> and <code>IMAGE_LOGO_HORIZONTAL</code>.</p>"""
    media_source: "aws_sdk_connect.types.media_source.MediaSource"
    """<p>The media source. Can be an S3 presigned URL or a base64-encoded string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportWorkspaceMediaRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.media_type

    out["MediaType"] = aws_sdk_connect.types.media_type.serialize_json(
        value["media_type"]
    )
    out["MediaSource"] = value["media_source"]
    return out


def deserialize_json(data: dict) -> ImportWorkspaceMediaRequest:
    out: ImportWorkspaceMediaRequest = {}  # type: ignore[typeddict-item]
    if "MediaType" in data:
        import aws_sdk_connect.types.media_type

        out["media_type"] = aws_sdk_connect.types.media_type.deserialize_json(
            data["MediaType"]
        )
    else:
        raise DeserializationError("ImportWorkspaceMediaRequest.media_type required")
    if "MediaSource" in data:
        out["media_source"] = data["MediaSource"]
    else:
        raise DeserializationError("ImportWorkspaceMediaRequest.media_source required")
    return out
