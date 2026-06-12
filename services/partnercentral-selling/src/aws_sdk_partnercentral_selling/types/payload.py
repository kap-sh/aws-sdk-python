"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#Payload``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_partnercentral_selling.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.lead_invitation_payload
    import aws_sdk_partnercentral_selling.types.opportunity_invitation_payload


class _Payload_OpportunityInvitation(TypedDict):
    OpportunityInvitation: "aws_sdk_partnercentral_selling.types.opportunity_invitation_payload.OpportunityInvitationPayload"


class _Payload_LeadInvitation(TypedDict):
    LeadInvitation: "aws_sdk_partnercentral_selling.types.lead_invitation_payload.LeadInvitationPayload"


Payload: TypeAlias = _Payload_OpportunityInvitation | _Payload_LeadInvitation


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Payload) -> dict:
    if "OpportunityInvitation" in value:
        import aws_sdk_partnercentral_selling.types.opportunity_invitation_payload

        return {
            "OpportunityInvitation": aws_sdk_partnercentral_selling.types.opportunity_invitation_payload.serialize_aws_json_1_0(
                value["OpportunityInvitation"]
            )
        }
    elif "LeadInvitation" in value:
        import aws_sdk_partnercentral_selling.types.lead_invitation_payload

        return {
            "LeadInvitation": aws_sdk_partnercentral_selling.types.lead_invitation_payload.serialize_aws_json_1_0(
                value["LeadInvitation"]
            )
        }
    else:
        raise SerializationError("Payload: no variant present")


def deserialize_aws_json_1_0(data: dict) -> Payload:
    if "OpportunityInvitation" in data:
        import aws_sdk_partnercentral_selling.types.opportunity_invitation_payload

        return {
            "OpportunityInvitation": aws_sdk_partnercentral_selling.types.opportunity_invitation_payload.deserialize_aws_json_1_0(
                data["OpportunityInvitation"]
            )
        }
    elif "LeadInvitation" in data:
        import aws_sdk_partnercentral_selling.types.lead_invitation_payload

        return {
            "LeadInvitation": aws_sdk_partnercentral_selling.types.lead_invitation_payload.deserialize_aws_json_1_0(
                data["LeadInvitation"]
            )
        }
    else:
        raise DeserializationError("Payload: no recognized variant key")
