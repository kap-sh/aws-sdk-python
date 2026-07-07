"""Generated from Smithy shape ``com.amazonaws.qapps#CreatePresignedUrlOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qapps.types.presigned_url_fields
    import aws_sdk_qapps.types.q_apps_timestamp


class CreatePresignedUrlOutput(TypedDict, closed=True):
    file_id: "str"
    """<p>The unique identifier assigned to the file to be uploaded.</p>"""
    presigned_url: "str"
    """<p>The URL for a presigned S3 POST operation used to upload a file.</p>"""
    presigned_url_fields: "aws_sdk_qapps.types.presigned_url_fields.PresignedUrlFields"
    """<p>The form fields to include in the presigned S3 POST operation used to upload a file.</p>"""
    presigned_url_expiration: "aws_sdk_qapps.types.q_apps_timestamp.QAppsTimestamp"
    """<p>The date and time that the presigned URL will expire in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePresignedUrlOutput) -> dict:
    out: dict = {}
    out["fileId"] = value["file_id"]
    out["presignedUrl"] = value["presigned_url"]
    import aws_sdk_qapps.types.presigned_url_fields

    out["presignedUrlFields"] = aws_sdk_qapps.types.presigned_url_fields.serialize_json(
        value["presigned_url_fields"]
    )
    import aws_sdk_qapps.types.q_apps_timestamp

    out["presignedUrlExpiration"] = aws_sdk_qapps.types.q_apps_timestamp.serialize_json(
        value["presigned_url_expiration"]
    )
    return out


def deserialize_json(data: dict) -> CreatePresignedUrlOutput:
    out: CreatePresignedUrlOutput = {}  # type: ignore[typeddict-item]
    if "fileId" in data:
        out["file_id"] = data["fileId"]
    else:
        raise DeserializationError("CreatePresignedUrlOutput.file_id required")
    if "presignedUrl" in data:
        out["presigned_url"] = data["presignedUrl"]
    else:
        raise DeserializationError("CreatePresignedUrlOutput.presigned_url required")
    if "presignedUrlFields" in data:
        import aws_sdk_qapps.types.presigned_url_fields

        out["presigned_url_fields"] = (
            aws_sdk_qapps.types.presigned_url_fields.deserialize_json(
                data["presignedUrlFields"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePresignedUrlOutput.presigned_url_fields required"
        )
    if "presignedUrlExpiration" in data:
        import aws_sdk_qapps.types.q_apps_timestamp

        out["presigned_url_expiration"] = (
            aws_sdk_qapps.types.q_apps_timestamp.deserialize_json(
                data["presignedUrlExpiration"]
            )
        )
    else:
        raise DeserializationError(
            "CreatePresignedUrlOutput.presigned_url_expiration required"
        )
    return out
