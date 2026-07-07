"""Generated from Smithy shape ``com.amazonaws.socialmessaging#GetWhatsAppMessageMediaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.s3_file
    import aws_sdk_socialmessaging.types.s3_presigned_url
    import aws_sdk_socialmessaging.types.whats_app_media_id
    import aws_sdk_socialmessaging.types.whats_app_phone_number_id


class GetWhatsAppMessageMediaInput(TypedDict, closed=True):
    media_id: "aws_sdk_socialmessaging.types.whats_app_media_id.WhatsAppMediaId"
    """<p>The unique identifier for the media file.</p>"""
    origination_phone_number_id: (
        "aws_sdk_socialmessaging.types.whats_app_phone_number_id.WhatsAppPhoneNumberId"
    )
    r"""<p>The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as <code>phone-number-id-01234567890123456789012345678901</code>. Use <a href=\"https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccount.html\">GetLinkedWhatsAppBusinessAccount</a> to find a phone number's id.</p>"""
    metadata_only: NotRequired["bool"]
    """<p>Set to <code>True</code> to get only the metadata for the file.</p>"""
    destination_s3_presigned_url: NotRequired[
        "aws_sdk_socialmessaging.types.s3_presigned_url.S3PresignedUrl"
    ]
    """<p>The presign url of the media file.</p>"""
    destination_s3_file: NotRequired["aws_sdk_socialmessaging.types.s3_file.S3File"]
    """<p>The <code>bucketName</code> and <code>key</code> of the S3 media file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWhatsAppMessageMediaInput) -> dict:
    out: dict = {}
    out["mediaId"] = value["media_id"]
    out["originationPhoneNumberId"] = value["origination_phone_number_id"]
    if "metadata_only" in value:
        out["metadataOnly"] = value["metadata_only"]
    if "destination_s3_presigned_url" in value:
        import aws_sdk_socialmessaging.types.s3_presigned_url

        out["destinationS3PresignedUrl"] = (
            aws_sdk_socialmessaging.types.s3_presigned_url.serialize_json(
                value["destination_s3_presigned_url"]
            )
        )
    if "destination_s3_file" in value:
        import aws_sdk_socialmessaging.types.s3_file

        out["destinationS3File"] = aws_sdk_socialmessaging.types.s3_file.serialize_json(
            value["destination_s3_file"]
        )
    return out


def deserialize_json(data: dict) -> GetWhatsAppMessageMediaInput:
    out: GetWhatsAppMessageMediaInput = {}  # type: ignore[typeddict-item]
    if "mediaId" in data:
        out["media_id"] = data["mediaId"]
    else:
        raise DeserializationError("GetWhatsAppMessageMediaInput.media_id required")
    if "originationPhoneNumberId" in data:
        out["origination_phone_number_id"] = data["originationPhoneNumberId"]
    else:
        raise DeserializationError(
            "GetWhatsAppMessageMediaInput.origination_phone_number_id required"
        )
    if "metadataOnly" in data:
        out["metadata_only"] = data["metadataOnly"]
    if "destinationS3PresignedUrl" in data:
        import aws_sdk_socialmessaging.types.s3_presigned_url

        out["destination_s3_presigned_url"] = (
            aws_sdk_socialmessaging.types.s3_presigned_url.deserialize_json(
                data["destinationS3PresignedUrl"]
            )
        )
    if "destinationS3File" in data:
        import aws_sdk_socialmessaging.types.s3_file

        out["destination_s3_file"] = (
            aws_sdk_socialmessaging.types.s3_file.deserialize_json(
                data["destinationS3File"]
            )
        )
    return out
