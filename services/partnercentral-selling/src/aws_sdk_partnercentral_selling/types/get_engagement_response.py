"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetEngagementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_arn
    import aws_sdk_partnercentral_selling.types.engagement_contexts
    import aws_sdk_partnercentral_selling.types.engagement_description
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.engagement_title


class GetEngagementResponse(TypedDict, closed=True):
    id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique resource identifier of the engagement retrieved.</p>"""
    arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_arn.EngagementArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the engagement retrieved.</p>"""
    title: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_title.EngagementTitle"
    ]
    """<p>The title of the engagement. It provides a brief, descriptive name for the engagement that is meaningful and easily recognizable.</p>"""
    description: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_description.EngagementDescription"
    ]
    """<p>A more detailed description of the engagement. This provides additional context or information about the engagement's purpose or scope.</p>"""
    created_at: NotRequired["aws_sdk_partnercentral_selling.types.date_time.DateTime"]
    r"""<p>The date and time when the Engagement was created, presented in ISO 8601 format (UTC). For example: \"2023-05-01T20:37:46Z\". This timestamp helps track the lifecycle of the Engagement.</p>"""
    created_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>The AWS account ID of the user who originally created the engagement. This field helps in tracking the origin of the engagement.</p>"""
    member_count: NotRequired["int"]
    """<p>Specifies the current count of members participating in the Engagement. This count includes all active members regardless of their roles or permissions within the Engagement.</p>"""
    modified_at: NotRequired["aws_sdk_partnercentral_selling.types.date_time.DateTime"]
    r"""<p>The timestamp indicating when the engagement was last modified, in ISO 8601 format (UTC). Example: \"2023-05-01T20:37:46Z\". This helps track the most recent changes to the engagement.</p>"""
    modified_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>The AWS account ID of the user who last modified the engagement. This field helps track who made the most recent changes to the engagement.</p>"""
    contexts: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_contexts.EngagementContexts"
    ]
    """<p>A list of context objects associated with the engagement. Each context provides additional information related to the Engagement, such as customer projects or documents.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetEngagementResponse) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "title" in value:
        out["Title"] = value["title"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_at" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["CreatedAt"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    if "member_count" in value:
        out["MemberCount"] = value["member_count"]
    if "modified_at" in value:
        import aws_sdk_partnercentral_selling.types.date_time

        out["ModifiedAt"] = (
            aws_sdk_partnercentral_selling.types.date_time.serialize_aws_json_1_0(
                value["modified_at"]
            )
        )
    if "modified_by" in value:
        out["ModifiedBy"] = value["modified_by"]
    if "contexts" in value:
        import aws_sdk_partnercentral_selling.types.engagement_contexts

        out["Contexts"] = (
            aws_sdk_partnercentral_selling.types.engagement_contexts.serialize_aws_json_1_0(
                value["contexts"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetEngagementResponse:
    out: GetEngagementResponse = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "CreatedAt" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["created_at"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "CreatedBy" in data:
        out["created_by"] = data["CreatedBy"]
    if "MemberCount" in data:
        out["member_count"] = data["MemberCount"]
    if "ModifiedAt" in data:
        import aws_sdk_partnercentral_selling.types.date_time

        out["modified_at"] = (
            aws_sdk_partnercentral_selling.types.date_time.deserialize_aws_json_1_0(
                data["ModifiedAt"]
            )
        )
    if "ModifiedBy" in data:
        out["modified_by"] = data["ModifiedBy"]
    if "Contexts" in data:
        import aws_sdk_partnercentral_selling.types.engagement_contexts

        out["contexts"] = (
            aws_sdk_partnercentral_selling.types.engagement_contexts.deserialize_aws_json_1_0(
                data["Contexts"]
            )
        )
    return out
