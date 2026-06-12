"""Generated from Smithy shape ``com.amazonaws.connect#StartContactRecordingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.voice_recording_configuration


class StartContactRecordingRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact.</p>"""
    initial_contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact. This is the identifier of the contact associated with the first interaction with the contact center.</p>"""
    voice_recording_configuration: "aws_sdk_connect.types.voice_recording_configuration.VoiceRecordingConfiguration"
    """<p>The person being recorded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartContactRecordingRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    out["InitialContactId"] = value["initial_contact_id"]
    import aws_sdk_connect.types.voice_recording_configuration

    out["VoiceRecordingConfiguration"] = (
        aws_sdk_connect.types.voice_recording_configuration.serialize_json(
            value["voice_recording_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> StartContactRecordingRequest:
    out: StartContactRecordingRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("StartContactRecordingRequest.instance_id required")
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("StartContactRecordingRequest.contact_id required")
    if "InitialContactId" in data:
        out["initial_contact_id"] = data["InitialContactId"]
    else:
        raise DeserializationError(
            "StartContactRecordingRequest.initial_contact_id required"
        )
    if "VoiceRecordingConfiguration" in data:
        import aws_sdk_connect.types.voice_recording_configuration

        out["voice_recording_configuration"] = (
            aws_sdk_connect.types.voice_recording_configuration.deserialize_json(
                data["VoiceRecordingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartContactRecordingRequest.voice_recording_configuration required"
        )
    return out
