"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadInvitationPayload``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.lead_invitation_customer
    import aws_sdk_partnercentral_selling.types.lead_invitation_interaction


class LeadInvitationPayload(TypedDict, closed=True):
    customer: "aws_sdk_partnercentral_selling.types.lead_invitation_customer.LeadInvitationCustomer"
    """<p>Contains information about the customer associated with the lead invitation. This data helps partners understand the customer's profile, industry, and business context to assess the lead opportunity.</p>"""
    interaction: "aws_sdk_partnercentral_selling.types.lead_invitation_interaction.LeadInvitationInteraction"
    """<p>Describes the interaction details associated with the lead, including the source of the lead generation and customer engagement information. This context helps partners evaluate the lead quality and engagement approach.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadInvitationPayload) -> dict:
    out: dict = {}
    import aws_sdk_partnercentral_selling.types.lead_invitation_customer

    out["Customer"] = (
        aws_sdk_partnercentral_selling.types.lead_invitation_customer.serialize_aws_json_1_0(
            value["customer"]
        )
    )
    import aws_sdk_partnercentral_selling.types.lead_invitation_interaction

    out["Interaction"] = (
        aws_sdk_partnercentral_selling.types.lead_invitation_interaction.serialize_aws_json_1_0(
            value["interaction"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadInvitationPayload:
    out: LeadInvitationPayload = {}  # type: ignore[typeddict-item]
    if "Customer" in data:
        import aws_sdk_partnercentral_selling.types.lead_invitation_customer

        out["customer"] = (
            aws_sdk_partnercentral_selling.types.lead_invitation_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    else:
        raise DeserializationError("LeadInvitationPayload.customer required")
    if "Interaction" in data:
        import aws_sdk_partnercentral_selling.types.lead_invitation_interaction

        out["interaction"] = (
            aws_sdk_partnercentral_selling.types.lead_invitation_interaction.deserialize_aws_json_1_0(
                data["Interaction"]
            )
        )
    else:
        raise DeserializationError("LeadInvitationPayload.interaction required")
    return out
