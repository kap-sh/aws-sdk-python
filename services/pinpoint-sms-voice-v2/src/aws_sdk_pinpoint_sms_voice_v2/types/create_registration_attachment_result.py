"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#CreateRegistrationAttachmentResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_sms_voice_v2.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_pinpoint_sms_voice_v2.types.attachment_status
    import aws_sdk_pinpoint_sms_voice_v2.types.tag_list


class CreateRegistrationAttachmentResult(TypedDict):
    registration_attachment_arn: "str"
    """<p>The Amazon Resource Name (ARN) for the registration attachment.</p>"""
    registration_attachment_id: "str"
    """<p>The unique identifier for the registration attachment.</p>"""
    attachment_status: (
        "aws_sdk_pinpoint_sms_voice_v2.types.attachment_status.AttachmentStatus"
    )
    """<p>The status of the registration attachment. </p> <ul> <li> <p> <code>UPLOAD_IN_PROGRESS</code> The attachment is being uploaded.</p> </li> <li> <p> <code>UPLOAD_COMPLETE</code> The attachment has been uploaded.</p> </li> <li> <p> <code>UPLOAD_FAILED</code> The attachment failed to uploaded.</p> </li> <li> <p> <code>DELETED</code> The attachment has been deleted..</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_pinpoint_sms_voice_v2.types.tag_list.TagList"]
    """<p>An array of tags (key and value pairs) to associate with the registration attachment.</p>"""
    created_timestamp: "datetime.datetime"
    r"""<p>The time when the registration attachment was created, in <a href=\"https://www.epochconverter.com/\">UNIX epoch time</a> format.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRegistrationAttachmentResult) -> dict:
    out: dict = {}
    out["RegistrationAttachmentArn"] = value["registration_attachment_arn"]
    out["RegistrationAttachmentId"] = value["registration_attachment_id"]
    out["AttachmentStatus"] = value["attachment_status"]
    if "tags" in value:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["Tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

    out["CreatedTimestamp"] = (
        aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.serialize_aws_json_1_0(
            value["created_timestamp"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRegistrationAttachmentResult:
    out: CreateRegistrationAttachmentResult = {}  # type: ignore[typeddict-item]
    if "RegistrationAttachmentArn" in data:
        out["registration_attachment_arn"] = data["RegistrationAttachmentArn"]
    else:
        raise DeserializationError(
            "CreateRegistrationAttachmentResult.registration_attachment_arn required"
        )
    if "RegistrationAttachmentId" in data:
        out["registration_attachment_id"] = data["RegistrationAttachmentId"]
    else:
        raise DeserializationError(
            "CreateRegistrationAttachmentResult.registration_attachment_id required"
        )
    if "AttachmentStatus" in data:
        out["attachment_status"] = data["AttachmentStatus"]
    else:
        raise DeserializationError(
            "CreateRegistrationAttachmentResult.attachment_status required"
        )
    if "Tags" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types.tag_list

        out["tags"] = (
            aws_sdk_pinpoint_sms_voice_v2.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    if "CreatedTimestamp" in data:
        import aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_pinpoint_sms_voice_v2.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    else:
        raise DeserializationError(
            "CreateRegistrationAttachmentResult.created_timestamp required"
        )
    return out
