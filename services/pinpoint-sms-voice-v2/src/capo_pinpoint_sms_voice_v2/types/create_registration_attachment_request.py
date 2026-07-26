"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRegistrationAttachmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.attachment_body
    import capo_pinpoint_sms_voice_v2.types.attachment_url
    import capo_pinpoint_sms_voice_v2.types.client_token
    import capo_pinpoint_sms_voice_v2.types.tag_list


class CreateRegistrationAttachmentRequest(TypedDict, closed=True):
    attachment_body: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.attachment_body.AttachmentBody"
    ]
    """<p>The registration file to upload. The maximum file size is 500KB and valid file extensions are PDF, JPEG and PNG.</p>"""
    attachment_url: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.attachment_url.AttachmentUrl"
    ]
    """<p>Registration files have to be stored in an Amazon S3 bucket. The URI to use when sending is in the format <code>s3://BucketName/FileName</code>.</p>"""
    tags: NotRequired["capo_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the registration attachment.</p>"""
    client_token: NotRequired[
        "capo_pinpoint_sms_voice_v2.types.client_token.ClientToken"
    ]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRegistrationAttachmentRequest) -> dict:
    out: dict = {}
    if "attachment_body" in value:
        import capo_pinpoint_sms_voice_v2.types.attachment_body

        out["AttachmentBody"] = (
            capo_pinpoint_sms_voice_v2.types.attachment_body.serialize_aws_json_1_0(
                value["attachment_body"]
            )
        )
    if "attachment_url" in value:
        out["AttachmentUrl"] = value["attachment_url"]
    if "tags" in value:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = capo_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRegistrationAttachmentRequest:
    out: CreateRegistrationAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "AttachmentBody" in data:
        import capo_pinpoint_sms_voice_v2.types.attachment_body

        out["attachment_body"] = (
            capo_pinpoint_sms_voice_v2.types.attachment_body.deserialize_aws_json_1_0(
                data["AttachmentBody"]
            )
        )
    if "AttachmentUrl" in data:
        out["attachment_url"] = data["AttachmentUrl"]
    if "Tags" in data:
        import capo_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            capo_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
