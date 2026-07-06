"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateEngagementContextResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_arn
    import aws_sdk_partnercentral_selling.types.engagement_context_identifier
    import aws_sdk_partnercentral_selling.types.engagement_identifier


class CreateEngagementContextResponse(TypedDict, closed=True):
    engagement_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique identifier of the engagement to which the context was added. This ID confirms the successful association of the context with the specified engagement.</p>"""
    engagement_arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_arn.EngagementArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the engagement to which the context was added. This globally unique identifier can be used for cross-service references and IAM policies.</p>"""
    engagement_last_modified_at: NotRequired[
        "aws_sdk_partnercentral_selling.types.date_time.DateTime"
    ]
    r"""<p>The timestamp indicating when the engagement was last modified as a result of adding the context, in ISO 8601 format (UTC). Example: \"2023-05-01T20:37:46Z\".</p>"""
    context_id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_context_identifier.EngagementContextIdentifier"
    ]
    """<p>The unique identifier assigned to the newly created engagement context. This ID can be used to reference the specific context within the engagement for future operations.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateEngagementContextResponse) -> dict:
    out: dict = {}
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "engagement_arn" in value:
        out["EngagementArn"] = value["engagement_arn"]
    if "engagement_last_modified_at" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["EngagementLastModifiedAt"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["engagement_last_modified_at"]
            )
        )
    if "context_id" in value:
        out["ContextId"] = value["context_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateEngagementContextResponse:
    out: CreateEngagementContextResponse = {}  # type: ignore[typeddict-item]
    if "EngagementId" in data:
        out["engagement_id"] = data["EngagementId"]
    if "EngagementArn" in data:
        out["engagement_arn"] = data["EngagementArn"]
    if "EngagementLastModifiedAt" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["engagement_last_modified_at"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["EngagementLastModifiedAt"]
            )
        )
    if "ContextId" in data:
        out["context_id"] = data["ContextId"]
    return out
