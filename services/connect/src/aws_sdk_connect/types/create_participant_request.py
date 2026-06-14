"""Generated from Smithy shape ``com.amazonaws.connect#CreateParticipantRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.contact_id
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.participant_details_to_add


class CreateParticipantRequest(TypedDict):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance. </p>"""
    contact_id: "aws_sdk_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact in this instance of Connect Customer. Supports contacts in the CHAT channel and VOICE (WebRTC) channels. For WebRTC calls, this should be the initial contact ID that was generated when the contact was first created (from the StartWebRTCContact API) in the VOICE channel</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""
    participant_details: (
        "aws_sdk_connect.types.participant_details_to_add.ParticipantDetailsToAdd"
    )
    """<p>Information identifying the participant.</p> <important> <p>The only valid value for <code>ParticipantRole</code> is <code>CUSTOM_BOT</code> for chat contact and <code>CUSTOMER</code> for voice contact.</p> </important>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateParticipantRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    out["ContactId"] = value["contact_id"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    import aws_sdk_connect.types.participant_details_to_add

    out["ParticipantDetails"] = (
        aws_sdk_connect.types.participant_details_to_add.serialize_json(
            value["participant_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateParticipantRequest:
    out: CreateParticipantRequest = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    else:
        raise DeserializationError("CreateParticipantRequest.instance_id required")
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("CreateParticipantRequest.contact_id required")
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "ParticipantDetails" in data:
        import aws_sdk_connect.types.participant_details_to_add

        out["participant_details"] = (
            aws_sdk_connect.types.participant_details_to_add.deserialize_json(
                data["ParticipantDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateParticipantRequest.participant_details required"
        )
    return out
