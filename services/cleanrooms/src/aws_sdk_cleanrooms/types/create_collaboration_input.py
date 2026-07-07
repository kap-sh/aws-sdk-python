"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateCollaborationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.allowed_result_regions
    import aws_sdk_cleanrooms.types.analytics_engine
    import aws_sdk_cleanrooms.types.auto_approved_change_type_list
    import aws_sdk_cleanrooms.types.collaboration_description
    import aws_sdk_cleanrooms.types.collaboration_job_log_status
    import aws_sdk_cleanrooms.types.collaboration_name
    import aws_sdk_cleanrooms.types.collaboration_query_log_status
    import aws_sdk_cleanrooms.types.data_encryption_metadata
    import aws_sdk_cleanrooms.types.display_name
    import aws_sdk_cleanrooms.types.member_abilities
    import aws_sdk_cleanrooms.types.member_list
    import aws_sdk_cleanrooms.types.ml_member_abilities
    import aws_sdk_cleanrooms.types.payment_configuration
    import aws_sdk_cleanrooms.types.tag_map


class CreateCollaborationInput(TypedDict, closed=True):
    members: "aws_sdk_cleanrooms.types.member_list.MemberList"
    """<p>A list of initial members, not including the creator. This list is immutable.</p>"""
    name: "aws_sdk_cleanrooms.types.collaboration_name.CollaborationName"
    """<p>The display name for a collaboration.</p>"""
    description: (
        "aws_sdk_cleanrooms.types.collaboration_description.CollaborationDescription"
    )
    """<p>A description of the collaboration provided by the collaboration owner.</p>"""
    creator_member_abilities: (
        "aws_sdk_cleanrooms.types.member_abilities.MemberAbilities"
    )
    """<p>The abilities granted to the collaboration creator.</p>"""
    creator_ml_member_abilities: NotRequired[
        "aws_sdk_cleanrooms.types.ml_member_abilities.MLMemberAbilities"
    ]
    """<p>The ML abilities granted to the collaboration creator.</p>"""
    creator_display_name: "aws_sdk_cleanrooms.types.display_name.DisplayName"
    """<p>The display name of the collaboration creator.</p>"""
    data_encryption_metadata: NotRequired[
        "aws_sdk_cleanrooms.types.data_encryption_metadata.DataEncryptionMetadata"
    ]
    """<p>The settings for client-side encryption with Cryptographic Computing for Clean Rooms.</p>"""
    query_log_status: "aws_sdk_cleanrooms.types.collaboration_query_log_status.CollaborationQueryLogStatus"
    """<p>An indicator as to whether query logging has been enabled or disabled for the collaboration.</p> <p>When <code>ENABLED</code>, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    job_log_status: NotRequired[
        "aws_sdk_cleanrooms.types.collaboration_job_log_status.CollaborationJobLogStatus"
    ]
    """<p>Specifies whether job logs are enabled for this collaboration. </p> <p>When <code>ENABLED</code>, Clean Rooms logs details about jobs run within this collaboration; those logs can be viewed in Amazon CloudWatch Logs. The default value is <code>DISABLED</code>.</p>"""
    tags: NotRequired["aws_sdk_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""
    creator_payment_configuration: NotRequired[
        "aws_sdk_cleanrooms.types.payment_configuration.PaymentConfiguration"
    ]
    """<p>The collaboration creator's payment responsibilities set by the collaboration creator. </p> <p>If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.</p>"""
    analytics_engine: NotRequired[
        "aws_sdk_cleanrooms.types.analytics_engine.AnalyticsEngine"
    ]
    """<p> The analytics engine.</p> <note> <p>After July 16, 2025, the <code>CLEAN_ROOMS_SQL</code> parameter will no longer be available. </p> </note>"""
    auto_approved_change_request_types: NotRequired[
        "aws_sdk_cleanrooms.types.auto_approved_change_type_list.AutoApprovedChangeTypeList"
    ]
    """<p>The types of change requests that are automatically approved for this collaboration.</p>"""
    allowed_result_regions: NotRequired[
        "aws_sdk_cleanrooms.types.allowed_result_regions.AllowedResultRegions"
    ]
    """<p>The Amazon Web Services Regions where collaboration query results can be stored. When specified, results can only be written to these Regions. This parameter enables you to meet your compliance and data governance requirements, and implement regional data governance policies.</p>"""
    is_metrics_enabled: NotRequired["bool"]
    """<p>An indicator as to whether metrics have been enabled or disabled for the collaboration.</p> <p>When <code>true</code>, collaboration members can opt in to Amazon CloudWatch metrics for their membership queries. The default value is <code>false</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCollaborationInput) -> dict:
    out: dict = {}
    import aws_sdk_cleanrooms.types.member_list

    out["members"] = aws_sdk_cleanrooms.types.member_list.serialize_json(
        value["members"]
    )
    out["name"] = value["name"]
    out["description"] = value["description"]
    import aws_sdk_cleanrooms.types.member_abilities

    out["creatorMemberAbilities"] = (
        aws_sdk_cleanrooms.types.member_abilities.serialize_json(
            value["creator_member_abilities"]
        )
    )
    if "creator_ml_member_abilities" in value:
        import aws_sdk_cleanrooms.types.ml_member_abilities

        out["creatorMLMemberAbilities"] = (
            aws_sdk_cleanrooms.types.ml_member_abilities.serialize_json(
                value["creator_ml_member_abilities"]
            )
        )
    out["creatorDisplayName"] = value["creator_display_name"]
    if "data_encryption_metadata" in value:
        import aws_sdk_cleanrooms.types.data_encryption_metadata

        out["dataEncryptionMetadata"] = (
            aws_sdk_cleanrooms.types.data_encryption_metadata.serialize_json(
                value["data_encryption_metadata"]
            )
        )
    import aws_sdk_cleanrooms.types.collaboration_query_log_status

    out["queryLogStatus"] = (
        aws_sdk_cleanrooms.types.collaboration_query_log_status.serialize_json(
            value["query_log_status"]
        )
    )
    if "job_log_status" in value:
        import aws_sdk_cleanrooms.types.collaboration_job_log_status

        out["jobLogStatus"] = (
            aws_sdk_cleanrooms.types.collaboration_job_log_status.serialize_json(
                value["job_log_status"]
            )
        )
    if "tags" in value:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.serialize_json(value["tags"])
    if "creator_payment_configuration" in value:
        import aws_sdk_cleanrooms.types.payment_configuration

        out["creatorPaymentConfiguration"] = (
            aws_sdk_cleanrooms.types.payment_configuration.serialize_json(
                value["creator_payment_configuration"]
            )
        )
    if "analytics_engine" in value:
        import aws_sdk_cleanrooms.types.analytics_engine

        out["analyticsEngine"] = (
            aws_sdk_cleanrooms.types.analytics_engine.serialize_json(
                value["analytics_engine"]
            )
        )
    if "auto_approved_change_request_types" in value:
        import aws_sdk_cleanrooms.types.auto_approved_change_type_list

        out["autoApprovedChangeRequestTypes"] = (
            aws_sdk_cleanrooms.types.auto_approved_change_type_list.serialize_json(
                value["auto_approved_change_request_types"]
            )
        )
    if "allowed_result_regions" in value:
        import aws_sdk_cleanrooms.types.allowed_result_regions

        out["allowedResultRegions"] = (
            aws_sdk_cleanrooms.types.allowed_result_regions.serialize_json(
                value["allowed_result_regions"]
            )
        )
    if "is_metrics_enabled" in value:
        out["isMetricsEnabled"] = value["is_metrics_enabled"]
    return out


def deserialize_json(data: dict) -> CreateCollaborationInput:
    out: CreateCollaborationInput = {}  # type: ignore[typeddict-item]
    if "members" in data:
        import aws_sdk_cleanrooms.types.member_list

        out["members"] = aws_sdk_cleanrooms.types.member_list.deserialize_json(
            data["members"]
        )
    else:
        raise DeserializationError("CreateCollaborationInput.members required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateCollaborationInput.name required")
    if "description" in data:
        out["description"] = data["description"]
    else:
        raise DeserializationError("CreateCollaborationInput.description required")
    if "creatorMemberAbilities" in data:
        import aws_sdk_cleanrooms.types.member_abilities

        out["creator_member_abilities"] = (
            aws_sdk_cleanrooms.types.member_abilities.deserialize_json(
                data["creatorMemberAbilities"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCollaborationInput.creator_member_abilities required"
        )
    if "creatorMLMemberAbilities" in data:
        import aws_sdk_cleanrooms.types.ml_member_abilities

        out["creator_ml_member_abilities"] = (
            aws_sdk_cleanrooms.types.ml_member_abilities.deserialize_json(
                data["creatorMLMemberAbilities"]
            )
        )
    if "creatorDisplayName" in data:
        out["creator_display_name"] = data["creatorDisplayName"]
    else:
        raise DeserializationError(
            "CreateCollaborationInput.creator_display_name required"
        )
    if "dataEncryptionMetadata" in data:
        import aws_sdk_cleanrooms.types.data_encryption_metadata

        out["data_encryption_metadata"] = (
            aws_sdk_cleanrooms.types.data_encryption_metadata.deserialize_json(
                data["dataEncryptionMetadata"]
            )
        )
    if "queryLogStatus" in data:
        import aws_sdk_cleanrooms.types.collaboration_query_log_status

        out["query_log_status"] = (
            aws_sdk_cleanrooms.types.collaboration_query_log_status.deserialize_json(
                data["queryLogStatus"]
            )
        )
    else:
        raise DeserializationError("CreateCollaborationInput.query_log_status required")
    if "jobLogStatus" in data:
        import aws_sdk_cleanrooms.types.collaboration_job_log_status

        out["job_log_status"] = (
            aws_sdk_cleanrooms.types.collaboration_job_log_status.deserialize_json(
                data["jobLogStatus"]
            )
        )
    if "tags" in data:
        import aws_sdk_cleanrooms.types.tag_map

        out["tags"] = aws_sdk_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    if "creatorPaymentConfiguration" in data:
        import aws_sdk_cleanrooms.types.payment_configuration

        out["creator_payment_configuration"] = (
            aws_sdk_cleanrooms.types.payment_configuration.deserialize_json(
                data["creatorPaymentConfiguration"]
            )
        )
    if "analyticsEngine" in data:
        import aws_sdk_cleanrooms.types.analytics_engine

        out["analytics_engine"] = (
            aws_sdk_cleanrooms.types.analytics_engine.deserialize_json(
                data["analyticsEngine"]
            )
        )
    if "autoApprovedChangeRequestTypes" in data:
        import aws_sdk_cleanrooms.types.auto_approved_change_type_list

        out["auto_approved_change_request_types"] = (
            aws_sdk_cleanrooms.types.auto_approved_change_type_list.deserialize_json(
                data["autoApprovedChangeRequestTypes"]
            )
        )
    if "allowedResultRegions" in data:
        import aws_sdk_cleanrooms.types.allowed_result_regions

        out["allowed_result_regions"] = (
            aws_sdk_cleanrooms.types.allowed_result_regions.deserialize_json(
                data["allowedResultRegions"]
            )
        )
    if "isMetricsEnabled" in data:
        out["is_metrics_enabled"] = data["isMetricsEnabled"]
    return out
