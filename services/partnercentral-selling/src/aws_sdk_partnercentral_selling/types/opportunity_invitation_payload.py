"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#OpportunityInvitationPayload``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.engagement_customer
    import aws_sdk_partnercentral_selling.types.project_details
    import aws_sdk_partnercentral_selling.types.receiver_responsibility_list
    import aws_sdk_partnercentral_selling.types.sender_contact_list


class OpportunityInvitationPayload(TypedDict):
    sender_contacts: NotRequired[
        "aws_sdk_partnercentral_selling.types.sender_contact_list.SenderContactList"
    ]
    """<p>Represents the contact details of the AWS representatives involved in sending the Engagement Invitation. These contacts are opportunity stakeholders.</p>"""
    receiver_responsibilities: "aws_sdk_partnercentral_selling.types.receiver_responsibility_list.ReceiverResponsibilityList"
    """<p>Outlines the responsibilities or expectations of the receiver in the context of the invitation.</p>"""
    customer: (
        "aws_sdk_partnercentral_selling.types.engagement_customer.EngagementCustomer"
    )
    """<p>Contains information about the customer related to the opportunity in the Engagement Invitation. This data helps partners understand the customer’s profile and requirements.</p>"""
    project: "aws_sdk_partnercentral_selling.types.project_details.ProjectDetails"
    """<p>Describes the project details associated with the opportunity, including the customer’s needs and the scope of work expected to be performed.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpportunityInvitationPayload) -> dict:
    out: dict = {}
    if "sender_contacts" in value:
        import aws_sdk_partnercentral_selling.types.sender_contact_list

        out["SenderContacts"] = (
            aws_sdk_partnercentral_selling.types.sender_contact_list.serialize_aws_json_1_0(
                value["sender_contacts"]
            )
        )
    import aws_sdk_partnercentral_selling.types.receiver_responsibility_list

    out["ReceiverResponsibilities"] = (
        aws_sdk_partnercentral_selling.types.receiver_responsibility_list.serialize_aws_json_1_0(
            value["receiver_responsibilities"]
        )
    )
    import aws_sdk_partnercentral_selling.types.engagement_customer

    out["Customer"] = (
        aws_sdk_partnercentral_selling.types.engagement_customer.serialize_aws_json_1_0(
            value["customer"]
        )
    )
    import aws_sdk_partnercentral_selling.types.project_details

    out["Project"] = (
        aws_sdk_partnercentral_selling.types.project_details.serialize_aws_json_1_0(
            value["project"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> OpportunityInvitationPayload:
    out: OpportunityInvitationPayload = {}  # type: ignore[typeddict-item]
    if "SenderContacts" in data:
        import aws_sdk_partnercentral_selling.types.sender_contact_list

        out["sender_contacts"] = (
            aws_sdk_partnercentral_selling.types.sender_contact_list.deserialize_aws_json_1_0(
                data["SenderContacts"]
            )
        )
    if "ReceiverResponsibilities" in data:
        import aws_sdk_partnercentral_selling.types.receiver_responsibility_list

        out["receiver_responsibilities"] = (
            aws_sdk_partnercentral_selling.types.receiver_responsibility_list.deserialize_aws_json_1_0(
                data["ReceiverResponsibilities"]
            )
        )
    else:
        raise DeserializationError(
            "OpportunityInvitationPayload.receiver_responsibilities required"
        )
    if "Customer" in data:
        import aws_sdk_partnercentral_selling.types.engagement_customer

        out["customer"] = (
            aws_sdk_partnercentral_selling.types.engagement_customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    else:
        raise DeserializationError("OpportunityInvitationPayload.customer required")
    if "Project" in data:
        import aws_sdk_partnercentral_selling.types.project_details

        out["project"] = (
            aws_sdk_partnercentral_selling.types.project_details.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    else:
        raise DeserializationError("OpportunityInvitationPayload.project required")
    return out
