"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#UpdateLeadContext``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_customer
    import capo_partnercentral_selling.types.lead_interaction
    import capo_partnercentral_selling.types.lead_qualification_status


class UpdateLeadContext(TypedDict, closed=True):
    qualification_status: "capo_partnercentral_selling.types.lead_qualification_status.LeadQualificationStatus"
    """<p>The updated qualification status of the lead.</p>"""
    customer: "capo_partnercentral_selling.types.lead_customer.LeadCustomer"
    """<p>Updated customer information associated with the lead.</p>"""
    interaction: NotRequired[
        "capo_partnercentral_selling.types.lead_interaction.LeadInteraction"
    ]
    """<p>Updated interaction details for the lead context.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateLeadContext) -> dict:
    out: dict = {}
    out["QualificationStatus"] = value.get("qualification_status", "Unqualified")
    import capo_partnercentral_selling.types.lead_customer

    out["Customer"] = (
        capo_partnercentral_selling.types.lead_customer.serialize_aws_json_1_0(
            value["customer"]
        )
    )
    if "interaction" in value:
        import capo_partnercentral_selling.types.lead_interaction

        out["Interaction"] = (
            capo_partnercentral_selling.types.lead_interaction.serialize_aws_json_1_0(
                value["interaction"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateLeadContext:
    out: UpdateLeadContext = {}  # type: ignore[typeddict-item]
    if "QualificationStatus" in data:
        out["qualification_status"] = data["QualificationStatus"]
    else:
        out["qualification_status"] = "Unqualified"
    if "Customer" in data:
        import capo_partnercentral_selling.types.lead_customer

        out["customer"] = (
            capo_partnercentral_selling.types.lead_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    else:
        raise DeserializationError("UpdateLeadContext.customer required")
    if "Interaction" in data:
        import capo_partnercentral_selling.types.lead_interaction

        out["interaction"] = (
            capo_partnercentral_selling.types.lead_interaction.deserialize_aws_json_1_0(
                data["Interaction"]
            )
        )
    return out
