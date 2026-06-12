"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AssignOpportunityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.assignee_contact
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_identifier


class AssignOpportunityRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is assigned in. Use <code>AWS</code> to assign real opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>"""
    identifier: "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    """<p>Requires the <code>Opportunity</code>'s unique identifier when you want to assign it to another user. Provide the correct identifier so the intended opportunity is reassigned.</p>"""
    assignee: "aws_sdk_partnercentral_selling.types.assignee_contact.AssigneeContact"
    """<p>Specifies the user or team member responsible for managing the assigned opportunity. This field identifies the <i>Assignee</i> based on the partner's internal team structure. Ensure that the email address is associated with a registered user in your Partner Central account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssignOpportunityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import aws_sdk_partnercentral_selling.types.assignee_contact

    out["Assignee"] = (
        aws_sdk_partnercentral_selling.types.assignee_contact.serialize_aws_json_1_0(
            value["assignee"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssignOpportunityRequest:
    out: AssignOpportunityRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("AssignOpportunityRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("AssignOpportunityRequest.identifier required")
    if "Assignee" in data:
        import aws_sdk_partnercentral_selling.types.assignee_contact

        out["assignee"] = (
            aws_sdk_partnercentral_selling.types.assignee_contact.deserialize_aws_json_1_0(
                data["Assignee"]
            )
        )
    else:
        raise DeserializationError("AssignOpportunityRequest.assignee required")
    return out
