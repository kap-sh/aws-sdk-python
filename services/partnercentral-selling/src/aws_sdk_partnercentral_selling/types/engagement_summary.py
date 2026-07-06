"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_account
    import aws_sdk_partnercentral_selling.types.date_time
    import aws_sdk_partnercentral_selling.types.engagement_arn
    import aws_sdk_partnercentral_selling.types.engagement_context_type_list
    import aws_sdk_partnercentral_selling.types.engagement_identifier
    import aws_sdk_partnercentral_selling.types.engagement_title


class EngagementSummary(TypedDict, closed=True):
    arn: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_arn.EngagementArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the created Engagement.</p>"""
    id: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p>The unique identifier for the Engagement.</p>"""
    title: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_title.EngagementTitle"
    ]
    """<p>The title of the Engagement.</p>"""
    created_at: NotRequired["aws_sdk_partnercentral_selling.types.date_time.DateTime"]
    """<p>The date and time when the Engagement was created.</p>"""
    created_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>The AWS Account ID of the Engagement creator.</p>"""
    member_count: NotRequired["int"]
    """<p>The number of members in the Engagement.</p>"""
    modified_at: NotRequired["aws_sdk_partnercentral_selling.types.date_time.DateTime"]
    r"""<p>The timestamp indicating when the engagement was last modified, in ISO 8601 format (UTC). Example: \"2023-05-01T20:37:46Z\".</p>"""
    modified_by: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_account.AwsAccount"
    ]
    """<p>The AWS account ID of the user who last modified the engagement. This field helps track who made the most recent changes to the engagement.</p>"""
    context_types: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_context_type_list.EngagementContextTypeList"
    ]
    r"""<p>An array of context types associated with the engagement, such as \"CustomerProject\" or \"Lead\". This provides a quick overview of the types of contexts included in the engagement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "id" in value:
        out["Id"] = value["id"]
    if "title" in value:
        out["Title"] = value["title"]
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
    if "context_types" in value:
        import aws_sdk_partnercentral_selling.types.engagement_context_type_list

        out["ContextTypes"] = (
            aws_sdk_partnercentral_selling.types.engagement_context_type_list.serialize_aws_json_1_0(
                value["context_types"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementSummary:
    out: EngagementSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Title" in data:
        out["title"] = data["Title"]
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
    if "ContextTypes" in data:
        import aws_sdk_partnercentral_selling.types.engagement_context_type_list

        out["context_types"] = (
            aws_sdk_partnercentral_selling.types.engagement_context_type_list.deserialize_aws_json_1_0(
                data["ContextTypes"]
            )
        )
    return out
