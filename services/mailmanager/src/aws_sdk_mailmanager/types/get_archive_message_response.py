"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetArchiveMessageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.envelope
    import aws_sdk_mailmanager.types.metadata
    import aws_sdk_mailmanager.types.s3_presigned_url


class GetArchiveMessageResponse(TypedDict):
    message_download_link: NotRequired[
        "aws_sdk_mailmanager.types.s3_presigned_url.S3PresignedURL"
    ]
    """<p>A pre-signed URL to temporarily download the full message content.</p>"""
    metadata: NotRequired["aws_sdk_mailmanager.types.metadata.Metadata"]
    """<p>The metadata about the email.</p>"""
    envelope: NotRequired["aws_sdk_mailmanager.types.envelope.Envelope"]
    """<p>The SMTP envelope information of the email.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetArchiveMessageResponse) -> dict:
    out: dict = {}
    if "message_download_link" in value:
        out["MessageDownloadLink"] = value["message_download_link"]
    if "metadata" in value:
        import aws_sdk_mailmanager.types.metadata

        out["Metadata"] = aws_sdk_mailmanager.types.metadata.serialize_aws_json_1_0(
            value["metadata"]
        )
    if "envelope" in value:
        import aws_sdk_mailmanager.types.envelope

        out["Envelope"] = aws_sdk_mailmanager.types.envelope.serialize_aws_json_1_0(
            value["envelope"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetArchiveMessageResponse:
    out: GetArchiveMessageResponse = {}  # type: ignore[typeddict-item]
    if "MessageDownloadLink" in data:
        out["message_download_link"] = data["MessageDownloadLink"]
    if "Metadata" in data:
        import aws_sdk_mailmanager.types.metadata

        out["metadata"] = aws_sdk_mailmanager.types.metadata.deserialize_aws_json_1_0(
            data["Metadata"]
        )
    if "Envelope" in data:
        import aws_sdk_mailmanager.types.envelope

        out["envelope"] = aws_sdk_mailmanager.types.envelope.deserialize_aws_json_1_0(
            data["Envelope"]
        )
    return out
