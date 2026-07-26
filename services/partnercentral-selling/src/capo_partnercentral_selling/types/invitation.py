"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Invitation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.invitation_message
    import capo_partnercentral_selling.types.payload
    import capo_partnercentral_selling.types.receiver


class Invitation(TypedDict, closed=True):
    message: "capo_partnercentral_selling.types.invitation_message.InvitationMessage"
    """<p> A message accompanying the invitation. </p>"""
    receiver: "capo_partnercentral_selling.types.receiver.Receiver"
    payload: "capo_partnercentral_selling.types.payload.Payload"


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Invitation) -> dict:
    out: dict = {}
    out["Message"] = value["message"]
    import capo_partnercentral_selling.types.receiver

    out["Receiver"] = capo_partnercentral_selling.types.receiver.serialize_aws_json_1_0(
        value["receiver"]
    )
    import capo_partnercentral_selling.types.payload

    out["Payload"] = capo_partnercentral_selling.types.payload.serialize_aws_json_1_0(
        value["payload"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> Invitation:
    out: Invitation = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    else:
        raise DeserializationError("Invitation.message required")
    if "Receiver" in data:
        import capo_partnercentral_selling.types.receiver

        out["receiver"] = (
            capo_partnercentral_selling.types.receiver.deserialize_aws_json_1_0(
                data["Receiver"]
            )
        )
    else:
        raise DeserializationError("Invitation.receiver required")
    if "Payload" in data:
        import capo_partnercentral_selling.types.payload

        out["payload"] = (
            capo_partnercentral_selling.types.payload.deserialize_aws_json_1_0(
                data["Payload"]
            )
        )
    else:
        raise DeserializationError("Invitation.payload required")
    return out
