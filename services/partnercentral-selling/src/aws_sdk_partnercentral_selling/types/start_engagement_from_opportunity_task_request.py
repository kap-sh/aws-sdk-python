"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#StartEngagementFromOpportunityTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_submission
    import aws_sdk_partnercentral_selling.types.catalog_identifier
    import aws_sdk_partnercentral_selling.types.client_token
    import aws_sdk_partnercentral_selling.types.opportunity_identifier
    import aws_sdk_partnercentral_selling.types.tag_list


class StartEngagementFromOpportunityTaskRequest(TypedDict, closed=True):
    catalog: "aws_sdk_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the engagement is tracked. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>"""
    client_token: "aws_sdk_partnercentral_selling.types.client_token.ClientToken"
    """<p>A unique token provided by the client to help ensure the idempotency of the request. It helps prevent the same task from being performed multiple times.</p>"""
    identifier: "aws_sdk_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    """<p>The unique identifier of the opportunity from which the engagement task is to be initiated. This helps ensure that the task is applied to the correct opportunity.</p>"""
    aws_submission: "aws_sdk_partnercentral_selling.types.aws_submission.AwsSubmission"
    tags: NotRequired["aws_sdk_partnercentral_selling.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartEngagementFromOpportunityTaskRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
    out["Identifier"] = value["identifier"]
    import aws_sdk_partnercentral_selling.types.aws_submission

    out["AwsSubmission"] = (
        aws_sdk_partnercentral_selling.types.aws_submission.serialize_aws_json_1_0(
            value["aws_submission"]
        )
    )
    if "tags" in value:
        import aws_sdk_partnercentral_selling.types.tag_list

        out["Tags"] = (
            aws_sdk_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
                value["tags"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartEngagementFromOpportunityTaskRequest:
    out: StartEngagementFromOpportunityTaskRequest = {}  # type: ignore[typeddict-item]
    if "Catalog" in data:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError(
            "StartEngagementFromOpportunityTaskRequest.catalog required"
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError(
            "StartEngagementFromOpportunityTaskRequest.client_token required"
        )
    if "Identifier" in data:
        out["identifier"] = data["Identifier"]
    else:
        raise DeserializationError(
            "StartEngagementFromOpportunityTaskRequest.identifier required"
        )
    if "AwsSubmission" in data:
        import aws_sdk_partnercentral_selling.types.aws_submission

        out["aws_submission"] = (
            aws_sdk_partnercentral_selling.types.aws_submission.deserialize_aws_json_1_0(
                data["AwsSubmission"]
            )
        )
    else:
        raise DeserializationError(
            "StartEngagementFromOpportunityTaskRequest.aws_submission required"
        )
    if "Tags" in data:
        import aws_sdk_partnercentral_selling.types.tag_list

        out["tags"] = (
            aws_sdk_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
