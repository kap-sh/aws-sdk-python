"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#DeleteRegistrationAttachmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_id_or_arn


class DeleteRegistrationAttachmentRequest(TypedDict):
    registration_attachment_id: "aws_sdk_pinpoint_sms_voice_v2.types.registration_attachment_id_or_arn.RegistrationAttachmentIdOrArn"
    """<p>The unique identifier for the registration attachment.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteRegistrationAttachmentRequest) -> dict:
    out: dict = {}
    out["RegistrationAttachmentId"] = value["registration_attachment_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteRegistrationAttachmentRequest:
    out: DeleteRegistrationAttachmentRequest = {}  # type: ignore[typeddict-item]
    if "RegistrationAttachmentId" in data:
        out["registration_attachment_id"] = data["RegistrationAttachmentId"]
    else:
        raise DeserializationError(
            "DeleteRegistrationAttachmentRequest.registration_attachment_id required"
        )
    return out
