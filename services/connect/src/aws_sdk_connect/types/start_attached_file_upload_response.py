"""Generated from Smithy shape ``com.amazonaws.connect#StartAttachedFileUploadResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.created_by_info
    import aws_sdk_connect.types.file_id
    import aws_sdk_connect.types.file_status_type
    import aws_sdk_connect.types.iso8601_datetime
    import aws_sdk_connect.types.upload_url_metadata


class StartAttachedFileUploadResponse(TypedDict):
    file_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The unique identifier of the attached file resource (ARN).</p>"""
    file_id: NotRequired["aws_sdk_connect.types.file_id.FileId"]
    """<p>The unique identifier of the attached file resource.</p>"""
    creation_time: NotRequired["aws_sdk_connect.types.iso8601_datetime.ISO8601Datetime"]
    """<p>The time of Creation of the file resource as an ISO timestamp. It's specified in ISO 8601 format: <code>yyyy-MM-ddThh:mm:ss.SSSZ</code>. For example, <code>2024-05-03T02:41:28.172Z</code>.</p>"""
    file_status: NotRequired["aws_sdk_connect.types.file_status_type.FileStatusType"]
    """<p>The current status of the attached file.</p>"""
    created_by: NotRequired["aws_sdk_connect.types.created_by_info.CreatedByInfo"]
    """<p>Represents the identity that created the file.</p>"""
    upload_url_metadata: NotRequired[
        "aws_sdk_connect.types.upload_url_metadata.UploadUrlMetadata"
    ]
    """<p>The headers to be provided while uploading the file to the URL.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAttachedFileUploadResponse) -> dict:
    out: dict = {}
    if "file_arn" in value:
        out["FileArn"] = value["file_arn"]
    if "file_id" in value:
        out["FileId"] = value["file_id"]
    if "creation_time" in value:
        out["CreationTime"] = value["creation_time"]
    if "file_status" in value:
        import aws_sdk_connect.types.file_status_type

        out["FileStatus"] = aws_sdk_connect.types.file_status_type.serialize_json(
            value["file_status"]
        )
    if "created_by" in value:
        import aws_sdk_connect.types.created_by_info

        out["CreatedBy"] = aws_sdk_connect.types.created_by_info.serialize_json(
            value["created_by"]
        )
    if "upload_url_metadata" in value:
        import aws_sdk_connect.types.upload_url_metadata

        out["UploadUrlMetadata"] = (
            aws_sdk_connect.types.upload_url_metadata.serialize_json(
                value["upload_url_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> StartAttachedFileUploadResponse:
    out: StartAttachedFileUploadResponse = {}  # type: ignore[typeddict-item]
    if "FileArn" in data:
        out["file_arn"] = data["FileArn"]
    if "FileId" in data:
        out["file_id"] = data["FileId"]
    if "CreationTime" in data:
        out["creation_time"] = data["CreationTime"]
    if "FileStatus" in data:
        import aws_sdk_connect.types.file_status_type

        out["file_status"] = aws_sdk_connect.types.file_status_type.deserialize_json(
            data["FileStatus"]
        )
    if "CreatedBy" in data:
        import aws_sdk_connect.types.created_by_info

        out["created_by"] = aws_sdk_connect.types.created_by_info.deserialize_json(
            data["CreatedBy"]
        )
    if "UploadUrlMetadata" in data:
        import aws_sdk_connect.types.upload_url_metadata

        out["upload_url_metadata"] = (
            aws_sdk_connect.types.upload_url_metadata.deserialize_json(
                data["UploadUrlMetadata"]
            )
        )
    return out
