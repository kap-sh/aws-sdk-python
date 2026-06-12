"""Generated from Smithy shape ``com.amazonaws.connect#ResumeContactRecordingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.contact_recording_type
    import aws_sdk_connect.types.instance_id


class ResumeContactRecordingRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    initial_contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.</p>"""
    contact_recording_type: NotRequired[
        "aws_sdk_connect.types.contact_recording_type.ContactRecordingType"
    ]
    """<p>The type of recording being operated on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResumeContactRecordingRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    out["InitialContactId"] = value["initial_contact_id"]
    if "contact_recording_type" in value:
        import aws_sdk_connect.types.contact_recording_type

        out["ContactRecordingType"] = (
            aws_sdk_connect.types.contact_recording_type.serialize_json(
                value["contact_recording_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResumeContactRecordingRequest:
    out: ResumeContactRecordingRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("ResumeContactRecordingRequest.instance_id required")
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("ResumeContactRecordingRequest.contact_id required")
    if "InitialContactId" in data:
        out["initial_contact_id"] = data["InitialContactId"]
    else:
        raise DeserializationError(
            "ResumeContactRecordingRequest.initial_contact_id required"
        )
    if "ContactRecordingType" in data:
        import aws_sdk_connect.types.contact_recording_type

        out["contact_recording_type"] = (
            aws_sdk_connect.types.contact_recording_type.deserialize_json(
                data["ContactRecordingType"]
            )
        )
    return out
