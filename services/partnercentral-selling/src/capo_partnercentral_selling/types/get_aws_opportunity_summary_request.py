"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetAwsOpportunitySummaryRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.opportunity_identifier


class GetAwsOpportunitySummaryRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the AWS Opportunity is located. Accepted values include <code>AWS</code> for production opportunities or <code>Sandbox</code> for testing purposes. The catalog determines which environment the opportunity data is pulled from.</p>"""
    related_opportunity_identifier: (
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    )
    """<p>The unique identifier for the related partner opportunity. Use this field to correlate an AWS opportunity with its corresponding partner opportunity.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetAwsOpportunitySummaryRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["RelatedOpportunityIdentifier"] = value["related_opportunity_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetAwsOpportunitySummaryRequest:
    out: GetAwsOpportunitySummaryRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("GetAwsOpportunitySummaryRequest.catalog required")
    if "RelatedOpportunityIdentifier" in data:
        out["related_opportunity_identifier"] = data["RelatedOpportunityIdentifier"]
    else:
        raise DeserializationError(
            "GetAwsOpportunitySummaryRequest.related_opportunity_identifier required"
        )
    return out
