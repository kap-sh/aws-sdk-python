"""Generated from Smithy shape ``com.amazonaws.socialmessaging#CreateWhatsAppMessageTemplateMediaInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_socialmessaging.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.linked_whats_app_business_account_id
    import aws_sdk_socialmessaging.types.s3_file


class CreateWhatsAppMessageTemplateMediaInput(TypedDict):
    id: "aws_sdk_socialmessaging.types.linked_whats_app_business_account_id.LinkedWhatsAppBusinessAccountId"
    """<p>The ID of the WhatsApp Business Account associated with this media upload.</p>"""
    source_s3_file: NotRequired["aws_sdk_socialmessaging.types.s3_file.S3File"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateWhatsAppMessageTemplateMediaInput) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "source_s3_file" in value:
        import aws_sdk_socialmessaging.types.s3_file

        out["sourceS3File"] = aws_sdk_socialmessaging.types.s3_file.serialize_json(
            value["source_s3_file"]
        )
    return out


def deserialize_json(data: dict) -> CreateWhatsAppMessageTemplateMediaInput:
    out: CreateWhatsAppMessageTemplateMediaInput = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError(
            "CreateWhatsAppMessageTemplateMediaInput.id required"
        )
    if "sourceS3File" in data:
        import aws_sdk_socialmessaging.types.s3_file

        out["source_s3_file"] = aws_sdk_socialmessaging.types.s3_file.deserialize_json(
            data["sourceS3File"]
        )
    return out
