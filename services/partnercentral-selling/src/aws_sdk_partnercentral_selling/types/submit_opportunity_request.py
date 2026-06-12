"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SubmitOpportunityRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.sales_involvement_type
    import aws_sdk_partnercentral_selling.types.visibility


class SubmitOpportunityRequest(TypedDict):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Submits the opportunity request from the production AWS environment.</p> </li> <li> <p>Sandbox: Submits the opportunity request from a sandbox environment used for testing or development purposes.</p> </li> </ul>"""
    identifier: "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    """<p>The identifier of the Opportunity previously created by partner and needs to be submitted.</p>"""
    involvement_type: "aws_sdk_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType"
    """<p>Specifies the level of AWS sellers' involvement on the opportunity. Valid values:</p> <ul> <li> <p> <code>Co-sell</code>: Indicates the user wants to co-sell with AWS. Share the opportunity with AWS to receive deal assistance and support.</p> </li> <li> <p> <code>For Visibility Only</code>: Indicates that the user does not need support from AWS Sales Rep. Share this opportunity with AWS for visibility only, you will not receive deal assistance and support.</p> </li> </ul>"""
    visibility: NotRequired[
        "aws_sdk_partnercentral_selling.types.visibility.Visibility"
    ]
    """<p>Determines whether to restrict visibility of the opportunity from AWS sales. Default value is Full. Valid values:</p> <ul> <li> <p> <code>Full</code>: The opportunity is fully visible to AWS sales.</p> </li> <li> <p> <code>Limited</code>: The opportunity has restricted visibility to AWS sales.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubmitOpportunityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import aws_sdk_partnercentral_selling.types.sales_involvement_type

    out["InvolvementType"] = (
        aws_sdk_partnercentral_selling.types.sales_involvement_type.serialize_aws_json_1_0(
            value["involvement_type"]
        )
    )
    if "visibility" in value:
        import aws_sdk_partnercentral_selling.types.visibility

        out["Visibility"] = (
            aws_sdk_partnercentral_selling.types.visibility.serialize_aws_json_1_0(
                value["visibility"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SubmitOpportunityRequest:
    out: SubmitOpportunityRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("SubmitOpportunityRequest.catalog required")
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError("SubmitOpportunityRequest.identifier required")
    if "InvolvementType" in data:
        import aws_sdk_partnercentral_selling.types.sales_involvement_type

        out["involvement_type"] = (
            aws_sdk_partnercentral_selling.types.sales_involvement_type.deserialize_aws_json_1_0(
                data["InvolvementType"]
            )
        )
    else:
        raise DeserializationError("SubmitOpportunityRequest.involvement_type required")
    if "Visibility" in data:
        import aws_sdk_partnercentral_selling.types.visibility

        out["visibility"] = (
            aws_sdk_partnercentral_selling.types.visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    return out
