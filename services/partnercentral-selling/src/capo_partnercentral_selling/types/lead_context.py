"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#LeadContext``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.lead_customer
    import capo_partnercentral_selling.types.lead_interaction_list
    import capo_partnercentral_selling.types.lead_qualification_status


class LeadContext(TypedDict, closed=True):
    qualification_status: "capo_partnercentral_selling.types.lead_qualification_status.LeadQualificationStatus"
    """<p>Indicates the current qualification status of the lead, such as whether it has been qualified, disqualified, or is still under evaluation. This helps track the lead's progression through the qualification process.</p>"""
    customer: "capo_partnercentral_selling.types.lead_customer.LeadCustomer"
    """<p>Contains detailed information about the customer associated with the lead, including company information, contact details, and other relevant customer data.</p>"""
    interactions: (
        "capo_partnercentral_selling.types.lead_interaction_list.LeadInteractionList"
    )
    """<p>An array of interactions that have occurred with the lead, providing a history of communications, meetings, and other engagement activities related to the lead.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LeadContext) -> dict:
    out: dict = {}
    out["QualificationStatus"] = value.get("qualification_status", "Unqualified")
    import capo_partnercentral_selling.types.lead_customer

    out["Customer"] = (
        capo_partnercentral_selling.types.lead_customer.serialize_aws_json_1_0(
            value["customer"]
        )
    )
    import capo_partnercentral_selling.types.lead_interaction_list

    out["Interactions"] = (
        capo_partnercentral_selling.types.lead_interaction_list.serialize_aws_json_1_0(
            value["interactions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> LeadContext:
    out: LeadContext = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("LeadContext.customer required")
    if "Interactions" in data:
        import capo_partnercentral_selling.types.lead_interaction_list

        out["interactions"] = (
            capo_partnercentral_selling.types.lead_interaction_list.deserialize_aws_json_1_0(
                data["Interactions"]
            )
        )
    else:
        raise DeserializationError("LeadContext.interactions required")
    return out
